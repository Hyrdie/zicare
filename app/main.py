import uvicorn

from orm import db
from orm.db_setup import database, engine
from fastapi import FastAPI
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
import logging
from contextlib import asynccontextmanager

db.metadata.create_all(engine)

async def startup():
    await database.connect()
    logger.info("zicare service is up!!!")

async def shutdown():
    await database.disconnect()
    logger.info("shutting down zicare service...")

@asynccontextmanager
async def lifespan(app:FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(title=settings.APP_NAME, docs_url=None, redoc_url=None, lifespan=lifespan)

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2222)