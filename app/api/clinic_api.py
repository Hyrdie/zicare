from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from app.service.clinic import create_clinic, get_clinic, get_clinic_by_id, delete_clinic, update_clinic
from .base_response import make_response
from .base import UnauthenticatedBaseApi
from fastapi.encoders import jsonable_encoder
from app.schema.clinic_schema import ClinicRequest, ClinicUpdateRequest
import logging

clinic_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(clinic_api)
class Clinic(UnauthenticatedBaseApi):
    @clinic_api.post('/clinic/')
    async def create_clinic(self, clinic:ClinicRequest):
        try:
            resp = create_clinic(clinic.name, clinic.address, clinic.doctor_name)
            logger.info(f"post /clinic endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"post /clinic endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @clinic_api.get('/clinic/')
    async def get_all_clinic(self):
        try:
            resp = get_clinic()
            logger.info(f"get /clinic endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /clinic endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @clinic_api.get('/clinic/{id}')
    async def get_all_clinic_by_id(self, id):
        try:
            resp = get_clinic_by_id(id)
            logger.info(f"get by id /clinic/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get by id /clinic/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @clinic_api.put('/clinic/{id}')
    async def update_clinic_by_id(self, id, clinic:ClinicUpdateRequest):
        try:
            resp = update_clinic(id, clinic.name, clinic.address, clinic.doctor_name)
            logger.info(f"update /clinic/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"update /clinic/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @clinic_api.delete('/clinic/{id}')
    async def delete_clinic_by_id(self, id):
        try:
            resp = delete_clinic(id)
            logger.info(f"delete by id /clinic/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"delete by id /clinic/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    