
FOUNDER_TEMPLATE = {
    "subject": "Interested in contributing to [Startup]",
    "body": """Hi [Founder Name],

I came across [Company] and was interested in the work you're doing around [specific product/domain]. With my experience in AI, Machine Learning, data analytics, and automation, I believe I could contribute to your team by building practical solutions, improving workflows, and turning complex data into actionable insights.

I have practical experience in building data-driven and AI-powered solutions. I've worked on a credit-risk prediction project involving over 2 million loan records, where I performed data analysis and developed models to identify borrowers at risk. I've also built an AI-powered invoice and purchase-order auditing system using OCR and LLMs to automate manual verification.
I'd love to explore how I could apply these skills at [Company], whether through analyzing business data, automating internal workflows, or developing AI-based tools that solve specific operational challenges. I'm not just looking for an internship title; I want the opportunity to take ownership of meaningful work, contribute to the team, and prove my value through results.
Would you be open to a brief conversation?

Best regards,
Mayank Arora
"""
}

RECRUITER_TEMPLATE = {
    "subject": "AI / ML Internship Opportunities at [Company]",
    "body": """Hi [Name],

I came across [Company] and was interested in the work your team is doing around [specific domain/product]. With my experience in AI, Machine Learning, data analytics, and automation, I believe I could contribute to your team by developing practical solutions and improving existing business workflows.

I have practical experience in building data-driven and AI-powered solutions. I've worked on a credit-risk prediction project involving over 2 million loan records, where I performed data analysis and developed models to identify borrowers at risk. I've also built an AI-powered invoice and purchase-order auditing system using OCR and LLMs to automate manual verification.

I'd love to explore how I could apply these skills at [company], whether through analyzing business data, automating internal workflows, or developing AI-based tools that solve specific operational challenges. I'm not just looking for an internship title; I want the opportunity to take ownership of meaningful work, contribute to the team, and prove my value through results.

Best regards,
Mayank Arora
"""
}

EMPLOYEE_TEMPLATE = {
    "subject": "Referral for AI / ML Opportunity at [Company]",
    "body": """Hi [Name],

I came across your profile while exploring [company] and wanted to reach out regarding potential opportunities to contribute to your team in AI, data analytics, or automation.

My technical experience includes Python, Machine Learning, Scikit-learn, LLM APIs, OCR, FastAPI, and SQL. I've applied these technologies in projects focused on solving practical business problems. One of my projects involved analyzing over 2 million loan records to identify borrowers at risk of default. I've also developed an AI-powered invoice and purchase-order auditing system that uses OCR and LLMs to extract information, automate verification, and reduce manual effort.

I'm particularly interested in exploring how AI and data-driven tools could support [company] business operations, from workflow automation to extracting useful insights from business data. I'd be keen to understand the challenges your team is currently working on and where my technical skills could be useful.

I'm looking for an opportunity to take ownership of real tasks, contribute to meaningful projects, and demonstrate my capabilities through results. If you feel my background aligns with any current or upcoming requirements, I'd really appreciate it if you could forward my resume to the relevant person in HR or the technical team.

Thank you for your time and consideration.

Best regards,
Mayank Arora
"""
}

def get_email_template(recipient_type: str):
    recipient_type = recipient_type.strip().lower()

    templates = {
        "founder": FOUNDER_TEMPLATE,
        "recruiter": RECRUITER_TEMPLATE,
        "cto": RECRUITER_TEMPLATE,
        "hr": RECRUITER_TEMPLATE,
        "employee": EMPLOYEE_TEMPLATE
    }

    return templates.get(recipient_type)
