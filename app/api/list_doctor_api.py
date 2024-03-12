from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base_response import make_response
from .base import UnauthenticatedBaseApi
from fastapi.encoders import jsonable_encoder
from app.schema.list_doctor_schema import ListDoctorSchema
from app.service.list_doctor_clinic import create_list_doctor, get_list_doctor_by_clinic_id, delete_list_doctor
import logging

list_doctor_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(list_doctor_api)
class ListDoctor(UnauthenticatedBaseApi):
    @list_doctor_api.post('/list-doctor')
    async def create_list_doctor(self, list_doctor:ListDoctorSchema):
        try:
            resp = create_list_doctor(list_doctor)
            logger.info(f"post /list-doctor endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"post /list-doctor endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)

    @list_doctor_api.get('/list-doctor/{clinic_id}')
    async def get_list_doctor(self, clinic_id):
        try:
            resp = get_list_doctor_by_clinic_id(clinic_id)
            logger.info(f"get /list-doctor endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"post /list-doctor endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @list_doctor_api.delete('/list-doctor/{clinic_id}/{doctor_id}')
    async def delete_list_doctor_by_id(self, clinic_id, doctor_id):
        try:
            resp = delete_list_doctor(clinic_id, doctor_id)
            logger.info(f"delete by id /list-doctor/{clinic_id}/{doctor_id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"delete by id /list-doctor/{clinic_id}/{doctor_id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)