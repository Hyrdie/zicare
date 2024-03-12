from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from app.orm.db_setup import get_db
from app.settings import settings

class BaseApi():
    db: Session = Depends(get_db)
    engine = create_engine(settings.DATABASE_URL)

    def make_response(self, payload: dict = {}, message: str = 'success', meta: dict = {}, code: int = 200):
        return JSONResponse(status_code=code, content={"message": message, "meta":meta, "data": payload})


class UnauthenticatedBaseApi(BaseApi):
    """
    Base class for unauthenticated route api
    """
    def __init__(self):
        super(UnauthenticatedBaseApi, self).__init__()