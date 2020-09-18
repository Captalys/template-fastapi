from ddtrace import patch_all
from ddtrace.contrib.asgi import TraceMiddleware

from fastapi import FastAPI

from src.resources.healthcheck import router as hc_router
from src.resources.crawler import router as crawler_router
from src.resources.credentials import router as credentials_router

patch_all()


app = FastAPI(title="{{cookiecutter.project_name}}", redoc_url=None)
app.add_middleware(TraceMiddleware)


app.include_router(crawler_router)
app.include_router(credentials_router)
app.include_router(hc_router)
