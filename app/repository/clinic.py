import sqlalchemy as sa
from app.orm.db import Clinic

def insert(session, name, address):
    sql = sa.insert(Clinic).values(
            name=name, 
            address=address, 
        ).returning(Clinic.c.id, Clinic.c.name)
    insert_clinic = session.execute(sql)
    session.commit()
    return insert_clinic

def get_all(session):
    sql = sa.select(
        Clinic
    )
    get_all_clinic = session.execute(sql)
    return get_all_clinic

def get_by_id(session, id):
    sql = sa.select(
        Clinic
    ).where(
        Clinic.c.id == id
    )
    get_clinic_by_id = session.execute(sql)
    return get_clinic_by_id

def update_name(session, id, name):
    sql = sa.update(
        Clinic
    ).where(
        Clinic.c.id == id
    ).values(
        name=name
    )
    updated_name = session.execute(sql)
    session.commit()
    return updated_name

def update_address(session, id, address):
    sql = sa.update(
        Clinic
    ).where(
        Clinic.c.id == id
    ).values(
        address=address
    )
    updated_name = session.execute(sql)
    session.commit()
    return updated_name

def update_list_doctor(session, id, doctor_name):
    sql = sa.update(
        Clinic
    ).where(
        Clinic.c.id == id
    ).values(
        list_doctor=doctor_name
    )
    updated_name = session.execute(sql)
    session.commit()
    return updated_name

def delete(session, id):
    sql = sa.delete(
        Clinic
    ).where(
        Clinic.c.id == id
    ).returning(
        Clinic.c.name
    )
    deleted = session.execute(sql)
    session.commit()
    return deleted