from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from os import getenv
import time
import uvicorn
from models.model import Base
from routes.router import router_basic

DB_URL = getenv('DB_URL')


@asynccontextmanager
async def lifespan(api=FastAPI):

    time.sleep(7) #ожидаем поднятия микросервиса с БД
    api.state.eng = create_engine(DB_URL)
    Base.metadata.create_all(api.state.eng)
    yield
    api.state.eng.dispose()

api = FastAPI(lifespan=lifespan)

#здесь подключим роутеры
api.include_router(router_basic)

if __name__ == '__main__':
    uvicorn.run(app='main:api', host='0.0.0.0', port=8000, reload=True)

