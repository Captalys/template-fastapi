from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/healthcheck", status_code=200)
def get_health():
    return JSONResponse(status_code=200, content=dict(message="I am alive."))
