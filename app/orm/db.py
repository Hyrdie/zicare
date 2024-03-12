from app.orm.db_setup import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime)

Clinic = Table(
    'clinic',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=True),
    Column('address', Text, nullable=True),
)

ListDoctorClinic = Table(
    'list_doctor_clinic',
    metadata,
    Column('clinic_id', Integer, ForeignKey("clinic.id"), nullable=False),
    Column('doctor_id', Integer, ForeignKey("doctor.id"), nullable=False)
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
    Column('end_time', Time, nullable=True)
)

Reservation = Table(
    'reservation',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('clinic_id', Integer, ForeignKey("clinic.id"), nullable=True),
    Column('doctor_id', Integer, ForeignKey("doctor.id"), nullable=True),
    Column('patient_id', Integer, ForeignKey("patient.id"), nullable=True),
    Column('operational_id', Integer, ForeignKey("operational_hours.id"), nullable=True),
    Column('date_time_reservation', DateTime, nullable=True),
    Column('status', Enum('scheduled','ongoing', 'canceled', 'done', name='status'), nullable=True),
    Column('queue_number', Integer, nullable=True)
)