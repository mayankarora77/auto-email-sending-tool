from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    company: str
    recipient_type: str

class EmailGenerateRequest(BaseModel):
    name: str
    email: EmailStr
    company: str
    recipient_type: str
    company_research: str