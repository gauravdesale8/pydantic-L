from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str = Field(max_length = 50)
    email: EmailStr
    lnkindUrl: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    married: bool
    allergies: Optional[List[str]] = Field(max_length=5) and None
    contact_details: Dict[str, str]



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into databases.")


patient_info = {'name':'Ramesh','email':'abc@gmail.com','lnkindUrl':'http://google.com/2343', 'age':30, 'weight':55.7, 'married': True, 'allergies': ['dust','pollen'], 'contact_details': {'email':'abc@gmail.com','phone':'234560'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)