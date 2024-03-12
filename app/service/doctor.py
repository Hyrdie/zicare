from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.doctor import (
    insert,
    get_all,
    get_by_id,
    update_name,
    update_specialize,
    delete
)
from app.schema.doctor_schema import DocterResponse, DocterDeletedResponse

def create_doctor(name, specialize):
    with Session(engine) as session:
        create_doctor_data = insert(session, name, specialize).fetchall()

    for value in create_doctor_data:
        id_doctor = value.id
    
    resp = DocterResponse(id=id_doctor, name=name, specialize=specialize)
    return resp

def get_doctor():
    resp = []
    with Session(engine) as session:
        doctor_data = get_all(session)
    
    for data in doctor_data:
        resp.append(DocterResponse(id=data.id, name=data.name, specialize=data.specialize))
    
    return resp

def get_doctor_by_id(id):
    with Session(engine) as session:
        doctor_data = get_by_id(session, id).fetchone()
    
    resp = DocterResponse(id=doctor_data.id, name=doctor_data.name, specialize=doctor_data.specialize)
    return resp

def update_doctor(id, name, specialize):
    with Session(engine) as session:
        if name != None:
            update_name(session, id, name)
            resp = DocterResponse(name="updated name : "+name)
            return resp
        if specialize != None:
            update_specialize(session, id, specialize)
            resp = DocterResponse(name="updated specialize : "+specialize)

def delete_doctor(id):
    with Session(engine) as session:
        deleted = delete(session, id).fetchone()
    return DocterDeletedResponse(id=id, detail="deleted docter with name : "+deleted.name)