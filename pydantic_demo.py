from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Inserted into databases.")


patient_info = {'name':'Ramesh', 'age':30}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)