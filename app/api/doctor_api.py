from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base_response import make_response
from .base import UnauthenticatedBaseApi
from fastapi.encoders import jsonable_encoder
from app.schema.doctor_schema import DocterRequest
from app.service.doctor import (
    create_doctor, get_doctor, get_doctor_by_id, update_doctor, delete_doctor
    )
import logging

doctor_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(doctor_api)
class Doctor(UnauthenticatedBaseApi):
    @doctor_api.post('/doctor/')
    async def create_doctor(self, doctor:DocterRequest):
        try:
            resp = create_doctor(doctor.name, doctor.specialize)
            logger.info(f"post /doctor endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"post /doctor endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @doctor_api.get('/doctor/')
    async def get_all_doctor(self):
        try:
            resp = get_doctor()
            logger.info(f"get /doctor endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /doctor endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @doctor_api.get('/doctor/{id}')
    async def get_doctor_by_id(self, id):
        try:
            resp = get_doctor_by_id(id)
            logger.info(f"get /doctor/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /doctor/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @doctor_api.put('/doctor/{id}')
    async def update_doctor(self, id, name, specialize):
        try:
            resp = update_doctor(id, name, specialize)
            logger.info(f"update /doctor/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"update /doctor/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @doctor_api.delete('/doctor/{id}')
    async def delete_doctor(self, id):
        try:
            resp = delete_doctor(id)
            logger.info(f"delete by id /doctor/{id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"delete by id /doctor/{id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
