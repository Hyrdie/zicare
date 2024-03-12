from pydantic import BaseModel
from datetime import datetime

class StatusReservation(BaseModel):
    scheduled = 'scheduled'
    ongoing = 'ongoing'
    canceled = 'canceled'
    done = 'done'

class ReservationSchema(BaseModel):
    clinic_id: int
    doctor_id: int
    patient_id: int
    operational_id: int
    date_time_reservation: datetime

class ReservationResponse(BaseModel):
    clinic: str
    doctor: str
    patient: str
    operational_hours: str
    date_time_reservation: datetime
    status: str
    queue_number: int

class ReservationUpdateResponse(BaseModel):
    detail: str

class ReservationFailedResponse(BaseModel):
    doctor: str
    clinic: str
    detail: str