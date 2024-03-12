from pydantic import BaseModel
from typing import List

class ListDoctorSchema(BaseModel):
    clinic_id:int
    doctor_id:int

class ListDoctor(BaseModel):
    doctor: str
    specialize: str

class ListDoctorResponse(BaseModel):
    clinic_name: str
    list_doctor: List[ListDoctor]

class ListDoctorDeletedResponse(BaseModel):
    detail: str