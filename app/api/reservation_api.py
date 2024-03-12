from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base_response import make_response
from .base import UnauthenticatedBaseApi
from fastapi.encoders import jsonable_encoder
from app.schema.reservation import ReservationSchema
from app.service.reservation import create_reservation, update_status_reservation
import logging

reservation_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(reservation_api)
class Reservation(UnauthenticatedBaseApi):
    @reservation_api.post('/reservation/')
    async def create_reservation(self, reservation:ReservationSchema):
        try:
            resp = create_reservation(reservation)
            logger.info(f"post /reservation endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"post /reservation endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
    
    @reservation_api.put('/reservation/{id}/{status}')
    async def update_reservation(self, id, status):
        try:
            resp = update_status_reservation(id, status)
            logger.info(f"put /reservation/{id}/{status} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"put /reservation/{id}/{status} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)