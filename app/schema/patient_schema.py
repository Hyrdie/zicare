from enum import Enum
from pydantic import BaseModel

class GenderEnum(str, Enum):
    male = "Male"
    female = 'Female'

class PaymentTypeEnum(str, Enum):
    personal = 'Personal'
    insurance = 'Insurance'

class PatientSchema(BaseModel):
    name: str
    age: str
    gender: GenderEnum
    username: str
    password: str
    payment_type: PaymentTypeEnum

class PatientResponse(BaseModel):
    id: int
    name: str
    payment_type: PaymentTypeEnum

class PatientDeletedResponse(BaseModel):
    id: int
    detail:str