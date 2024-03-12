import sqlalchemy as sa
from app.schema.reservation import ReservationSchema
from app.orm.db import Reservation
from sqlalchemy import func

def insert(session, data:ReservationSchema, queue_number, status):
    sql = sa.insert(
        Reservation
    ).values(
        clinic_id=data.clinic_id,
        doctor_id=data.doctor_id,
        patient_id=data.patient_id,
        operational_id=data.operational_id,
        date_time_reservation=data.date_time_reservation,
        status=status,
        queue_number=queue_number
    ).returning(
        Reservation
    )
    insert_reservation = session.execute(sql)
    session.commit()
    return insert_reservation

def count_queue_number(session):
    sql = sa.select([func.count(Reservation.c.id).label('queue_number')]).filter(
        Reservation.c.status == 'scheduled'
    )
    total_count = session.execute(sql)
    return total_count

def update_status(session, id, status):
    sql = sa.update(
        Reservation
    ).where(
        Reservation.c.id == id
    ).values(
        status = status
    ).returning(
        Reservation
    )
    update_reservation_status = session.execute(sql)
    return update_reservation_status