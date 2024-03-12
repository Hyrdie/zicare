import sqlalchemy as sa
from app.orm.db import Doctor

def insert(session, name, specialize):
    sql = sa.insert(Doctor).values(
        name=name,
        specialize=specialize
    ).returning(Doctor.c.id, Doctor.c.name)
    insert_doctor = session.execute(sql)
    session.commit()
    return insert_doctor

def get_all(session):
    sql = sa.select(Doctor)
    get_all_doctor = session.execute(sql)
    return get_all_doctor

def get_by_id(session, id):
    sql = sa.select(
        Doctor
    ).where(
        Doctor.c.id == id
    )
    get_docter_by_id = session.execute(sql)
    return get_docter_by_id

def update_name(session, id, name):
    sql = sa.update(
        Doctor
    ).where(
        Doctor.c.id == id
    ).values(
        name=name
    )
    updated_name = session.execute(sql)
    session.commit()
    return updated_name

def update_specialize(session, id, specialize):
    sql = sa.update(
        Doctor
    ).where(
        Doctor.c.id == id
    ).values(
        specialize=specialize
    )
    updated_specialize = session.execute(sql)
    session.commit()
    return updated_specialize

def delete(session, id):
    sql = sa.delete(
        Doctor
    ).where(
        Doctor.c.id == id
    ).returning(
        Doctor.c.name
    )
    deleted = session.execute(sql)
    session.commit()
    return deleted