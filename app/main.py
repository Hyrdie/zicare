import uvicorn
import logging

from app.orm import db
import sqlalchemy as sa
from sqlalchemy.orm import Session
from app.orm.db_setup import database, engine
from fastapi import FastAPI
from app.settings import settings
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.clinic_api import clinic_api
from app.api.doctor_api import doctor_api
from app.api.patient_api import patient_api
from app.api.operational_hours_api import operational_hours
from app.api.list_doctor_api import list_doctor_api
from app.api.reservation_api import reservation_api

db.metadata.create_all(engine)

clinic_data = sa.insert(db.Clinic).values([
    {"name":"Zicare Clinic", "address":"Jakarta"},
    {"name":"Hyrdie Clinic", "address":"Bekasi"}
])
doctor_data = sa.insert(db.Doctor).values([
    {"name":"Dr. Verstappen", "specialize":"Saraf"},
    {"name":"Dr. Checo", "specialize":"Bedah"},
    {"name":"Dr. Albon", "specialize":"Kandungan"},
    {"name":"Dr. Vettel", "specialize":"Kulit"},
    {"name":"Dr. Danric", "specialize":"Penyakit Dalam"},
    {"name":"Dr. Yuki", "specialize":"Anak"}
])
patient_data = sa.insert(db.Patient).values([
    {"name":"Hamilton", "age":"20", "gender":"Male", "username":"ham", "password":"4321lupa", "payment_type":"Personal"},
    {"name":"George", "age":"21", "gender":"Male", "username":"geo", "password":"4321lupa", "payment_type":"Insurance"},
    {"name":"Kevin", "age":"22", "gender":"Male", "username":"kev", "password":"4321lupa", "payment_type":"Personal"},
    {"name":"Zhuan", "age":"23", "gender":"Male", "username":"zhu", "password":"4321lupa", "payment_type":"Insurance"},
    {"name":"Kamal", "age":"24", "gender":"Male", "username":"mal", "password":"4321lupa", "payment_type":"Personal"},
])
list_doctor_data = sa.insert(db.ListDoctorClinic).values([
    {"clinic_id":"1", "doctor_id":"1"},
    {"clinic_id":"2", "doctor_id":"2"},
    {"clinic_id":"1", "doctor_id":"3"},
    {"clinic_id":"2", "doctor_id":"4"},
    {"clinic_id":"1", "doctor_id":"5"},
    {"clinic_id":"2", "doctor_id":"1"}
])



async def startup():
    await database.connect()
    with Session(engine) as session:
        session.execute(clinic_data)
        session.execute(doctor_data)
        session.execute(patient_data)
        session.execute(list_doctor_data)
        session.commit()
    logger.info("zicare service is up!!!")

async def shutdown():
    await database.disconnect()
    logger.info("shutting down zicare service...")

@asynccontextmanager
async def lifespan(app:FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

origins = settings.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS
)

@app.get("/alive")
async def getInfo():
    return {
        "desc":"Microservices for zicare reservation"
    }

app.include_router(clinic_api, tags=["Clinic"])
app.include_router(doctor_api, tags=["Doctor"])
app.include_router(list_doctor_api, tags=["List Doctor"])
app.include_router(patient_api, tags=["Patient"])
app.include_router(operational_hours, tags=["Operational Hours"])
app.include_router(reservation_api, tags=["Reservation"])