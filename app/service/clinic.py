from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.clinic import (
    insert, 
    get_all, 
    get_by_id, 
    update_name, 
    update_list_doctor, 
    update_address, 
    delete
) 
from app.schema.clinic_schema import ClinicResponse, ClinicDeleteResponse

def create_clinic(name, address):
    with Session(engine) as session:
        create_clinic_data = insert(session, name, address).fetchall()
    
    for value in create_clinic_data:
        id_clinic = value.id
    
    resp = ClinicResponse(id=id_clinic, name=name, address=address)

    return resp

def get_clinic():
    resp = []
    with Session(engine) as session:
        clinic_data = get_all(session).fetchall()
    
    for data in clinic_data:
        resp.append(ClinicResponse(id=data.id, name=data.name, address=data.name))

    return resp

def get_clinic_by_id(id):
    with Session(engine) as session:
        clinic_data = get_by_id(session, id).fetchone()
    
    resp = ClinicResponse(id=clinic_data.id, name=clinic_data.name, address=clinic_data.address)
    return resp

def update_clinic(id, name, address, doctor_name):
    with Session(engine) as session:
        if name != None:
            update_name(session, id, name)
            resp = ClinicResponse(name="updated name : "+name)
            return resp
        if address != None:
            update_address(session, id, address)
            resp = ClinicResponse(address="updated address : "+address)
            return resp
        if doctor_name != None:
            update_list_doctor(session, id, doctor_name)
            resp = ClinicResponse(address="updated list doctor : "+doctor_name)

def delete_clinic(id):
    with Session(engine) as session:
       deleted = delete(session, id).fetchone()
    return ClinicDeleteResponse(id=id, detail="deleted clinic with name : "+deleted.name)


