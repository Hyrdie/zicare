from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.operational_hours import (
    insert,
    get_by_id,
    get_by_clinic_id,
    get_by_doctor_id,
    delete
)
from app.service.doctor import get_doctor_by_id
from app.service.clinic import get_clinic_by_id
from app.schema.operational_hours_schema import (
    OperationalSchema, 
    OperationalResponse, 
    OperationalResponseByClinic, 
    ListDoctor, 
    ListClinic, 
    OperationalResponseByDoctor,
    DeletedResponse
)

def create_operational_hours(data:OperationalSchema):
    with Session(engine) as session:
        insert(session, data)

    doctor_data = get_doctor_by_id(data.doctor_id)
    clinic_data = get_clinic_by_id(data.clinic_id)
    
    resp = OperationalResponse(
        doctor=doctor_data.name, 
        clinic=clinic_data.name, 
        day=data.day, 
        start_time=data.start_time, 
        end_time=data.end_time
        )
    return resp

def get_operational_by_id(id):
    with Session(engine) as session:
        operational_by_id = get_by_id(session, id).fetchone()
    
    return operational_by_id


def get_operational_by_clinic_id(clinic_id):
    resp = []
    with Session(engine) as session:
        operational_by_clinic_id = get_by_clinic_id(session, clinic_id).fetchall()
    
    if not operational_by_clinic_id:
        return resp
        
    list_doctor = []
    for data in operational_by_clinic_id:
        doctor_data = get_doctor_by_id(data.doctor_id)
        clinic_data = get_clinic_by_id(data.clinic_id)
        list_doctor.append(ListDoctor(
            doctor=doctor_data.name, specialize=doctor_data.specialize, day=data.day, 
            start_time=data.start_time, end_time=data.end_time
            ))

    if clinic_data:
        resp.append(OperationalResponseByClinic(
            clinic=clinic_data.name, list_doctor=list_doctor
        ))
    
    return resp

def get_operational_by_doctor_id(doctor_id):
    resp = []
    with Session(engine) as session:
        operational_by_doctor_id = get_by_doctor_id(session, doctor_id).fetchall()
    
    if not operational_by_doctor_id:
        return resp
        
    list_clinic = []
    for data in operational_by_doctor_id:
        doctor_data = get_doctor_by_id(data.doctor_id)
        clinic_data = get_clinic_by_id(data.clinic_id)
        list_clinic.append(ListClinic(
            clinic=clinic_data.name, address=clinic_data.address, day=data.day, 
            start_time=data.start_time, end_time=data.end_time
            ))

    if clinic_data:
        resp.append(OperationalResponseByDoctor(
            doctor=doctor_data.name, list_clinic=list_clinic
        ))
    
    return resp

def delete_operational_hours(clinic_id, doctor_id):
    with Session(engine) as session:
        deleted = delete(session, clinic_id, doctor_id).fetchone()
    
    doctor_data = get_doctor_by_id(deleted.doctor_id)
    clinic_data = get_clinic_by_id(deleted.clinic_id)

    return DeletedResponse(detail=f"removing operation hours with doctor name : {doctor_data.name} in {clinic_data.name}")