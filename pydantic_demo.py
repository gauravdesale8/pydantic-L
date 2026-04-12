from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length = 50, title='Name of that person.',description='Give the name in max 50 characters.', examples=['Amit','Mahesh'])]
    email: EmailStr
    lnkindUrl: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float,Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None,description='Is patient married or not?')]
    allergies: Annotated[Optional[List[str]],Field(default=None, max_length=5)]
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