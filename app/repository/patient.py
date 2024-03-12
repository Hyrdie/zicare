import sqlalchemy as sa
from app.orm.db import Patient
from app.schema.patient_schema import PatientSchema

def insert(session, data:PatientSchema):
    sql = sa.insert(Patient).values(
        name=data.name,
        age=data.age,
        gender=data.gender,
        username=data.username,
        password=data.password,
        payment_type=data.payment_type
    ).returning(Patient.c.id, Patient.c.name)
    insert_patient = session.execute(sql)
    session.commit()
    return insert_patient

def get_all(session):
    sql = sa.select(Patient)
    get_all_patient = session.execute(sql)
    return get_all_patient

def get_by_id(session, id):
    sql = sa.select(
        Patient
    ).where(
        Patient.c.id == id
    )
    get_patient_by_id = session.execute(sql)
    return get_patient_by_id

def update(session, id, data:PatientSchema):
    sql = sa.update(
        Patient
    ).where(
        Patient.c.id == id
    ).values(
        name=data.name,
        age=data.age,
        gender=data.gender,
        username=data.username,
        password=data.password,
        payment_type=data.payment_type
    )
    update_patient = session.execute(sql)
    session.commit()
    return update_patient

def delete(session, id):
    sql = sa.delete(
        Patient
    ).where(
        Patient.c.id == id
    ).returning(
        Patient.c.name
    )
    deleted = session.execute(sql)
    session.commit()
    return deleted