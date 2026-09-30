
import gradio as gr
import requests
import re
from email.message import EmailMessage
from pathlib import Path
import os
import smtplib
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent / ".env", override=True)


# Resume location
RESUME_PATH = r"C:\Users\Mayank\OneDrive\Desktop\resume.pdf"

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/generate-email"


def generate_email(name, email, company, recipient_type, company_research):
    payload = {
        "name": name,
        "email": email,
        "company": company,
        "recipient_type": recipient_type,
        "company_research": company_research
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=120)
        response.raise_for_status()

        result = response.json()
        raw_email = result["generated_email"].strip()

        subject_match = re.search(
            r"(?im)^Subject:\s*(.*)$",
            raw_email
        )

        body_match = re.search(
            r"(?im)^Body:\s*",
            raw_email
        )

        subject = subject_match.group(1).strip() if subject_match else ""

        if body_match:
            body = raw_email[body_match.end():].strip()
        else:
            body = raw_email

        if not body_match and subject_match:
            body = re.sub(
                r"(?im)^Subject:.*(?:\n|$)",
                "",
                raw_email,
                count=1
            ).strip()

        return subject, body

    except requests.exceptions.HTTPError as e:
        return "", f"API error: {response.text}"

    except requests.exceptions.RequestException as e:
        return "", f"Connection error: {e}"
    except (ValueError, KeyError) as e:
        return "", f"Could not process the API response: {e}"

def autofill_from_email(email_address, current_name, current_company):
    if not email_address or "@" not in email_address:
        return current_name, current_company

    try:
        local_part, domain = email_address.strip().lower().split("@", 1)

        if not local_part or "." not in domain:
            return current_name, current_company

        # Convert chitranshu.gupta or chitranshu_gupta to Chitranshu Gupta
        name_part = local_part.split("+", 1)[0]
        name = re.sub(r"[._-]+", " ", name_part).title()

        # Convert primeos.in to Primeos
        company_part = domain.split(".")[0]
        company = company_part.replace("-", " ").title()

        return name, company

    except ValueError:
        return current_name, current_company


def attach_resume(msg):
    resume_path = Path(RESUME_PATH)

    if not resume_path.is_file():
        raise FileNotFoundError(
            f"Resume not found at: {resume_path}"
        )

    msg.add_attachment(
        resume_path.read_bytes(),
        maintype="application",
        subtype="pdf",
        filename=resume_path.name
    )
def send_email(recipient_email, subject, body):
    gmail_address = os.getenv("GMAIL_ADDRESS", "").strip()
    gmail_app_password = os.getenv("GMAIL_APP_PASSWORD", "").strip().replace(" ", "")

    

    if not gmail_address or not gmail_app_password:
        return "Error: Gmail credentials are missing from .env"

    try:
        msg = EmailMessage()
        msg["From"] = gmail_address
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach your resume automatically
        attach_resume(msg)

        # Send through Gmail
        with smtplib.SMTP_SSL(
    "smtp.gmail.com",
    465,
    timeout=30
    ) as server:
            server.login(gmail_address, gmail_app_password)
            server.send_message(msg)

        return "Email sent successfully with resume attached!"

    except Exception as e:
        return f"Error sending email: {e}"

with gr.Blocks(title="AI Cold Email Generator") as demo:

    gr.Markdown("# AI Cold Email Generator")
    gr.Markdown("Generate personalized cold emails using AI.")

    name = gr.Textbox(
        label="Recipient Name",
        placeholder="e.g. Rahul Sharma"
    )

    email = gr.Textbox(
        label="Recipient Email",
        placeholder="e.g. rahul@company.com"
    )

    company = gr.Textbox(
        label="Company Name",
        placeholder="e.g. NovoStack"
    )

    recipient_type = gr.Dropdown(
        choices=["Founder", "Recruiter", "HR", "CTO"],
        label="Recipient Type",
        value="Founder"
    )

    company_research = gr.Textbox(
        label="Company Research",
        placeholder="Paste your verified company research here...",
        lines=5
    )
    email.change(
    fn=autofill_from_email,
    inputs=[email, name, company],
    outputs=[name, company]
    )

    generate_button = gr.Button(
        "Generate Email",
        variant="primary"
    )

    subject = gr.Textbox(
        label="Email Subject",
        placeholder="Generated subject will appear here...",
        lines=1,
        interactive=True
    )

    body = gr.Textbox(
        label="Email Body",
        placeholder="Generated email body will appear here...",
        lines=15,
        interactive=True
    )

    generate_button.click(
        fn=generate_email,
        inputs=[
            name,
            email,
            company,
            recipient_type,
            company_research
        ],
        outputs=[subject, body]
    )
    send_button = gr.Button(
    "Send Email",
    variant="primary"
    )

    send_status = gr.Textbox(
        label="Sending Status",
        interactive=False
    )

    send_button.click(
        fn=send_email,
        inputs=[email, subject, body],
        outputs=send_status
    )

demo.launch(server_port=7860)