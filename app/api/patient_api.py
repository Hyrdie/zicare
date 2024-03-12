from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base_response import make_response
from .base import UnauthenticatedBaseApi
from fastapi.encoders import jsonable_encoder
from app.schema.patient_schema import PatientSchema
from app.service.patient import create_patient, get_patient, get_patient_by_id, update_patient, delete_patient
import logging

patient_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(patient_api)
class Patient(UnauthenticatedBaseApi):
    @patient_api.post('/patient/')
    async def create_patient(self, patient:PatientSchema):
        try:
            resp = create_patient(patient)
            logger.info(f"post /patient endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"post /patient endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)

    @patient_api.get('/patient/')
    async def get_all_patient(self):
        try:
            resp = get_patient()
            logger.info(f"get /patient endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /patient endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @patient_api.get('/patient/{id}')
    async def get_patient_by_id(self, id):
        try:
            resp = get_patient_by_id(id)
            logger.info(f"get /patient/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /patient/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @patient_api.put('/patient/{id}')
    async def update_patient(self, id, data:PatientSchema):
        try:
            resp = update_patient(id, data)
            logger.info(f"update /patient/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /patient/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @patient_api.delete('/patient/{id}')
    async def delete_patient(self, id):
        try:
            resp = delete_patient(id)
            logger.info(f"delete by id /patient/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"delete /patient/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
