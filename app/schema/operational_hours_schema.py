from pydantic import BaseModel
from datetime import time
from typing import List

class OperationalSchema(BaseModel):
    doctor_id:int
    clinic_id:int
    day: str
    start_time: time
    end_time: time

class OperationalResponse(BaseModel):
    doctor:str
    clinic:str
    day: str
    start_time: time
    end_time: time

class ListDoctor(BaseModel):
    doctor: str
    specialize: str
    day: str
    start_time: time
    end_time: time

class ListClinic(BaseModel):
    clinic: str
    address: str
    day: str
    start_time: time
    end_time: time

class OperationalResponseByClinic(BaseModel):
    clinic: str
    list_doctor: List[ListDoctor]

class OperationalResponseByDoctor(BaseModel):
    doctor:str
    list_clinic:List[ListClinic]

class DeletedResponse(BaseModel):
    detail:str