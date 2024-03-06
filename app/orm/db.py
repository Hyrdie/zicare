from orm.db_setup import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime)

Clinic = Table(
    'clinic',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=True),
    Column('address', Text, nullable=True),
    Column('list_doctor', JSON, nullable=True)
)

Patient = Table(
    'patient',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('age', Integer, nullable=True),
    Column('gender', Enum('Male','Female', name='gender'), nullable=True),
    Column('username', String, nullable=True),
    Column('password', String, nullable=True),
    Column('payment_type', Enum('Personal','Insurance', name='payment_type'), nullable=True)
)

Doctor = Table(
    'doctor',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('specialize', String, nullable=True)
)

OperationalHours = Table(
    'operational_hours',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('doctor_id', Integer, ForeignKey("doctor.id"), nullable=True),
    Column('clinic_id', Integer, ForeignKey("clinic.id"), nullable=True),
    Column('day', String, nullable=True),
    Column('start_time', Time, nullable=True),
    Column('ent_time', Time, nullable=True)
)

Reservation = Table(
    'reservation',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('clinic_id', Integer, ForeignKey("clinic.id"), nullable=True),
    Column('doctor_id', Integer, ForeignKey("doctor.id"), nullable=True),
    Column('patient_id', Integer, ForeignKey("patient.id"), nullable=True),
    Column('operational_id', Integer, ForeignKey("operational_hours.id"), nullable=True),
    Column('date_time_reservation', DateTime, nullable=True)
)