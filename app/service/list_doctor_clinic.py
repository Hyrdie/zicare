from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.list_doctor_clinic import (
    insert,
    get_by_clinic_id,
    delete
)
from app.service.clinic import get_clinic_by_id
from app.service.doctor import get_doctor_by_id
from app.schema.list_doctor_schema import ListDoctorSchema, ListDoctorResponse, ListDoctor, ListDoctorDeletedResponse

def create_list_doctor(data:ListDoctorSchema):
    with Session(engine) as session:
        insert(session, data).fetchall()
    
    resp = ListDoctorSchema(clinic_id=data.clinic_id, doctor_id=data.doctor_id)
    return resp

def get_list_doctor_by_clinic_id(clinic_id):
    with Session(engine) as session:
        list_doctor_data = get_by_clinic_id(session, clinic_id).fetchall()
    
    list_doctor = []
    for value in list_doctor_data:
        doctor_data = get_doctor_by_id(value.doctor_id)
        clinic_data = get_clinic_by_id(value.clinic_id)
        list_doctor.append(ListDoctor(doctor=doctor_data.name, specialize=doctor_data.specialize))
    
    resp = ListDoctorResponse(clinic_name=clinic_data.name, list_doctor=list_doctor)
    return resp

def delete_list_doctor(clinic_id, doctor_id):
    with Session(engine) as session:
        deleted = delete(session, clinic_id, doctor_id).fetchone()

    doctor_data = get_doctor_by_id(deleted.doctor_id)
    clinic_data = get_clinic_by_id(deleted.clinic_id)

    return ListDoctorDeletedResponse(detail=f"removing doctor with name : {doctor_data.name} from {clinic_data.name}")
