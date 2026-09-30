from groq_client import generate_email

response = generate_email(
    "Write one short sentence saying hello to Mayank."
)

print(response)