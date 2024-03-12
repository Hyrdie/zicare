from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.patient import (
    insert,
    get_all,
    get_by_id,
    update,
    delete
)
from app.schema.patient_schema import PatientSchema, PatientResponse, PatientDeletedResponse

def create_patient(data:PatientSchema):
    with Session(engine) as session:
        create_patient_data = insert(session, data).fetchall()
    
    for value in create_patient_data:
        id_patient = value.id
    
    resp = PatientResponse(id=id_patient, name=data.name, payment_type=data.payment_type)
    return resp

def get_patient():
    resp = []
    with Session(engine) as session:
        patient_data = get_all(session)
    
    for data in patient_data:
        resp.append(PatientResponse(id=data.id, name=data.name, payment_type=data.payment_type))
    
    return resp

def get_patient_by_id(id):
    with Session(engine) as session:
        patient_data = get_by_id(session, id).fetchone()
    
    resp = PatientResponse(
        id=patient_data.id, name=patient_data.name, payment_type=patient_data.payment_type
        )
    
    return resp

def update_patient(id, data:PatientSchema):
    with Session(engine) as session:
        update(session, id, data)
    
    resp = PatientResponse(id=id, name=data.name, payment_type=data.payment_type)
    return resp

def delete_patient(id):
    with Session(engine) as session:
        deleted = delete(session, id).fetchone()
    if not deleted:
        return PatientDeletedResponse(id=0, detail="There is no id to delete")
    return PatientDeletedResponse(id=id, detail="deleted patient with name : "+deleted.name)


