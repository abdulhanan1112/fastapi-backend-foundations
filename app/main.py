from fastapi import FastAPI, status
from app.api.routers.students import router


app=FastAPI(
    title='Student API',
    version='1.0.0'
)

app.include_router(
    router,
)