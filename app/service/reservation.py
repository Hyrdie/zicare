from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.reservation import (
    insert,
    count_queue_number,
    update_status
)
from app.service.clinic import get_clinic_by_id
from app.service.doctor import get_doctor_by_id
from app.service.patient import get_patient_by_id
from app.service.operational_hours import get_operational_by_id

from app.schema.reservation import ReservationSchema, ReservationResponse, ReservationFailedResponse, ReservationUpdateResponse

def create_reservation(data:ReservationSchema):
    queue_number = 0
    
    clinic_data = get_clinic_by_id(data.clinic_id)
    doctor_data = get_doctor_by_id(data.doctor_id)
    patient_data = get_patient_by_id(data.patient_id)
    operational_data = get_operational_by_id(data.operational_id)

    time_reservation = data.date_time_reservation.strftime('%H:%M')
    if time_reservation > operational_data.end_time.strftime('%H:%M') or time_reservation < operational_data.start_time.strftime('%H:%M'):
        resp = ReservationFailedResponse(
            doctor=doctor_data.name,
            clinic=clinic_data.name,
            detail=f"Doctor : {doctor_data.name} is not available at this hour in {clinic_data.name}"
        )
        return resp

    with Session(engine) as session:
        status = 'scheduled'
        count_data = count_queue_number(session).fetchone()
        queue_number = count_data.queue_number + 1
        insert(session, data, queue_number, status)
    
    resp = ReservationResponse(
        clinic=clinic_data.name,
        doctor=doctor_data.name,
        patient=patient_data.name,
        operational_hours=operational_data.day,
        date_time_reservation=data.date_time_reservation,
        status=status,
        queue_number=queue_number
    )

    return resp

def update_status_reservation(id, status):
    with Session(engine) as session:
        data = update_status(session, id, status).fetchone()

    clinic_data = get_clinic_by_id(data.clinic_id)
    patient_data = get_patient_by_id(data.patient_id)
    resp = ReservationUpdateResponse(
        detail=f"patient {patient_data.name} has done the appointment in {clinic_data.name}"
    )
    return resp

