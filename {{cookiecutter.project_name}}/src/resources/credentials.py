from aiohttp import ClientSession
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.exceptions import *
from src.core.crawler import Crawler
from src.utils.urls import URL_MAPPING
from src.models import LocalSession
from src.models.scorpion import LogSystem, Warranty
from src.schemas import ValidateLoginPayload, validate_login_responses

router = APIRouter()


@router.post("/validate-login", responses=validate_login_responses)
async def get_flow(payload: ValidateLoginPayload):
    try:
        async with ClientSession() as session:
            crawler = Crawler(session, url_mapping=URL_MAPPING)
            await crawler.login(payload.document_number, payload.login, payload.password)
        return JSONResponse(status_code=200, content=dict(message="SUCCESS"))
    except LoginInvalidoException:
        return JSONResponse(status_code=401, content=dict(message="INVALID_PASSWORD"))
    except CNPJInvalidoException:
        return JSONResponse(status_code=401, content=dict(message="INVALID_CNPJ"))
    except InstabilidadeNoAdquirente:
        return JSONResponse(status_code=502, content=dict(message="ERROR_ADQ"))
    except Exception as e:
        """
            Caso ocorra uma exceção inesperada no sistema, tenta
            gravar no banco de dados do scorpion.
        """
        session = LocalSession()
        warrant_id = Warranty.get_warranty_id(session)
        if warrant_id:
            LogSystem(
                document_number=payload.document_number,
                warranty_id=warrant_id, message=str(e)[:99]
            ).save(session)
        session.close()
        return JSONResponse(status_code=500, content=dict(message=str(e)))