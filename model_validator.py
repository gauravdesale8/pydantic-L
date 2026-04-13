from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    lnkindUrl: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients more than age 60 should have emergency contact.")
        return model

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.weight)
    print(patient.allergies)
    print("Inserted into databases.")


patient_info = {'name':'Ramesh','email':'abc@axis.com','lnkindUrl':'http://google.com/2343', 'age':'65', 'weight':55.7, 'married': True, 'allergies': ['dust','pollen'], 'contact_details': {'email':'abc@gmail.com','phone':'234560','emergency':'2345210'}}

patient1 = Patient(**patient_info)  # validation -> type coercion

insert_patient_data(patient1)