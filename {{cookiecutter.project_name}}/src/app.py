from ddtrace import patch_all
from ddtrace.contrib.asgi import TraceMiddleware

from fastapi import FastAPI

from src.routes.healthcheck import router as hc_router
from src.routes.example import router as ex_router


patch_all()


app = FastAPI(title="{{cookiecutter.project_name}}", redoc_url=None, openapi_url='/swagger.json')
app.add_middleware(TraceMiddleware)


app.include_router(ex_router, prefix="api/")
app.include_router(hc_router, prefix="api/")
