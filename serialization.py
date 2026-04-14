from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pin: str
    

class Patient(BaseModel):

    name: str
    age: str = 30
    gender: str
    address: Address


address_dict = {"city":"Mumbai","state":"Maharashtra","pin":"400001"}

address1 = Address(**address_dict)   #unpacking of dict

patient_dict = {"name":"Ashris","gender":"male","address":address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include=['name','gender'])
temp1 = patient1.model_dump_json(exclude={'address':['state']})
temp2 = patient1.model_dump(exclude_unset=True)

print(temp)
print(temp1)
print(temp2)
print(type(temp))
print(type(temp1))