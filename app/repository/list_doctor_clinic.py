from app.orm.db import ListDoctorClinic
import sqlalchemy as sa
from app.schema.list_doctor_schema import ListDoctorSchema

def insert(session, data:ListDoctorSchema):
    sql = sa.insert(ListDoctorClinic).values(
        clinic_id=data.clinic_id,
        doctor_id=data.doctor_id
    ).returning(ListDoctorClinic.c.clinic_id, ListDoctorClinic.c.doctor_id)
    insert_list_doctor = session.execute(sql)
    session.commit()
    return insert_list_doctor

def get_by_clinic_id(session, clinic_id):
    sql = sa.select(
        ListDoctorClinic
    ).where(
        ListDoctorClinic.c.clinic_id == clinic_id
    ).group_by(
        ListDoctorClinic.c.clinic_id, ListDoctorClinic.c.doctor_id
    )
    get_list_doctor_by_clinic_id = session.execute(sql)
    return get_list_doctor_by_clinic_id

def delete(session, clinic_id, doctor_id):
    sql = sa.delete(
        ListDoctorClinic
    ).where(
        sa.and_(
            ListDoctorClinic.c.clinic_id == clinic_id,
            ListDoctorClinic.c.doctor_id == doctor_id
        )
    ).returning(
        ListDoctorClinic.c.clinic_id, ListDoctorClinic.c.doctor_id
    )
    deleted = session.execute(sql)
    session.commit()
    return deleted

