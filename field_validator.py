from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com','axis.com','hsbc.co.in']
        # abc@gmail.com

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Invalid domain name")
        

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Invalid age')


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.weight)
    print(patient.allergies)
    print("Inserted into databases.")


patient_info = {'name':'Ramesh','email':'abc@axis.com','lnkindUrl':'http://google.com/2343', 'age':30, 'weight':55.7, 'married': True, 'allergies': ['dust','pollen'], 'contact_details': {'email':'abc@gmail.com','phone':'234560'}}

patient1 = Patient(**patient_info)  # validation -> type coercion

insert_patient_data(patient1)