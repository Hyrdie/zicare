from app.orm.db import OperationalHours
from app.schema.operational_hours_schema import OperationalSchema
import sqlalchemy as sa

def insert(session, data:OperationalSchema):
    sql = sa.insert(OperationalHours).values(
        doctor_id=data.doctor_id,
        clinic_id=data.clinic_id,
        day=data.day,
        start_time=data.start_time,
        end_time=data.end_time
    ).returning(OperationalHours)
    insert_operational_hours = session.execute(sql)
    session.commit()
    return insert_operational_hours

def get_by_id(session, id):
    sql = sa.select(
        OperationalHours
    ).where(
        OperationalHours.c.id == id
    )
    get_operational_by_id = session.execute(sql)
    return get_operational_by_id

def get_by_clinic_id(session, clinic_id):
    sql = sa.select(
        OperationalHours
    ).where(
        OperationalHours.c.clinic_id == clinic_id
    ).group_by(
        OperationalHours.c.clinic_id, OperationalHours.c.doctor_id, OperationalHours.c.id
    )
    get_operational_by_clinic_id = session.execute(sql)
    return get_operational_by_clinic_id

def get_by_doctor_id(session, doctor_id):
    sql = sa.select(
        OperationalHours
    ).where(
        OperationalHours.c.doctor_id == doctor_id
    ).group_by(
        OperationalHours.c.clinic_id, OperationalHours.c.doctor_id, OperationalHours.c.id
    )
    get_operational_by_doctor_id = session.execute(sql)
    return get_operational_by_doctor_id


def delete(session, clinic_id, doctor_id):
    sql = sa.delete(
        OperationalHours
    ).where(
        sa.and_(
            OperationalHours.c.clinic_id == clinic_id,
            OperationalHours.c.doctor_id == doctor_id
        )
    ).returning(
        OperationalHours.c.clinic_id, OperationalHours.c.doctor_id
    )
    deleted = session.execute(sql)
    session.commit()
    return deleted