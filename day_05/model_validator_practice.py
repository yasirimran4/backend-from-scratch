from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    model_validator,
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

    # @model_validator(mode="before")    # Before creating model it's a dictionary
    # def check_patient_contact(cls, model):
    #     if model.get("age", 0) > 60 and "emergency" not in model.get("contact", {}):
    #         raise ValueError("Patient older than 60 should have emergency contact")
    #     return model

    @model_validator(mode="after")  # After creating model it's a model
    def check_patient_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact:
            raise ValueError("Patient older than 60 should have emergency contact")
        return model


app = FastAPI()


# @app.post("/patients")
# def create_patient(patient: Patient):
#     return patient


patient = {
    "name": "yasir imran",
    "age": 62,
    "weight": 44.9,
    "email": "yasirdev@cili.com",
    "linkedin_url": "https://linkedin.com",
    "contact": {"email": "yasirimran.com", "phone": "56789", "emergency": "56789"},
}

patient1 = Patient(**patient)

print(patient1)
