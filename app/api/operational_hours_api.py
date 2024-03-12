from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base_response import make_response
from .base import UnauthenticatedBaseApi
from fastapi.encoders import jsonable_encoder
from app.schema.operational_hours_schema import OperationalSchema
from app.service.operational_hours import create_operational_hours, get_operational_by_clinic_id, get_operational_by_doctor_id, delete_operational_hours
import logging

operational_hours = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(operational_hours)
class OperationalHours(UnauthenticatedBaseApi):
    @operational_hours.post('/operational-hours/')
    async def create_operational_hours(self, operational_hours:OperationalSchema):
        try:
            resp = create_operational_hours(operational_hours)
            logger.info(f"post /operational-hours endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"post /operational-hours endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @operational_hours.get('/operational-hours-clinic/{clinic_id}')
    async def get_operational_hours_by_clinic_id(self, clinic_id):
        try:
            resp = get_operational_by_clinic_id(clinic_id)
            logger.info(f"get /operational-hours-clinic endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /operational-hours-clinic endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @operational_hours.get('/operational-hours-doctor/{doctor_id}')
    async def get_operational_hours_by_doctor_id(self, doctor_id):
        try:
            resp = get_operational_by_doctor_id(doctor_id)
            logger.info(f"get /operational-hours-doctor endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get /operational-hours-doctor endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @operational_hours.delete('/operational-hours/{clinic_id}/{doctor_id}')
    async def delete_operational_hours_by_id(self, clinic_id, doctor_id):
        try:
            resp = delete_operational_hours(clinic_id, doctor_id)
            logger.info(f"delete by id /operational-hours/{clinic_id}/{doctor_id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"delete by id /operational-hours/{clinic_id}/{doctor_id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
