from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    field_validator,
    AnyUrl,
)
from fastapi import FastAPI
from typing import Annotated, List, Dict, Optional


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50,
            title="Name of Patient",
            description="Name should be less than 50 chars",
        ),
    ]
    email: Annotated[
        EmailStr, Field(title="Patient Email", description="Give valid Patient Email")
    ]
    age: Annotated[
        int,
        Field(gt=0, le=120, title="Patient Age", description="Age should be positive"),
    ]
    weight: Annotated[
        float, Field(gt=0, description="Weight cannot be negetive", strict=True)
    ]
    married: Annotated[bool, Field(default=False)]
    linkedin_url: Annotated[
        AnyUrl, Field(title="Linkedin URL", description="Patient Linkedin url")
    ]
    allergies: Annotated[Optional[List[str]], Field(default=None)]
    contact: Dict[str, str]

    @field_validator("email")
    @classmethod
    def check_patient_email(cls, value):
        valid_domains = ["cili.com", "apex.com"]

        domain = value.split("@")[-1]

        if domain not in valid_domains:
            raise ValueError("Not a valid domain")

        return value

    @field_validator("name")
    @classmethod
    def capiltalize_name(cls, value):
        return value.capitalize()


app = FastAPI()


# @app.post("/patients")
# def create_patient(patient: Patient):
#     return patient


patient = {
    "name": "yasi imran",
    "age": 12,
    "weight": 44.9,
    "email": "yasirdev@cili.com",
    "linkedin_url": "https://linkedin.com",
    "contact": {"email": "yasirimran.com", "phone": "56789"},
}

patient1 = Patient(**patient)

print(patient1)
