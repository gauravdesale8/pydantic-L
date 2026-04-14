from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    lnkindUrl: AnyUrl
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        calculate_bmi = round(self.weight/(self.height**2),2)
        return calculate_bmi

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.weight)
    print(patient.allergies)
    print("BMI", patient.bmi)
    print("Inserted into databases.")


patient_info = {'name':'Ramesh','email':'abc@axis.com','lnkindUrl':'http://google.com/2343', 'age':'65', 'weight':55.7,'height':'1.24', 'married': True, 'allergies': ['dust','pollen'], 'contact_details': {'email':'abc@gmail.com','phone':'234560','emergency':'2345210'}}

patient1 = Patient(**patient_info)  # validation -> type coercion

insert_patient_data(patient1)