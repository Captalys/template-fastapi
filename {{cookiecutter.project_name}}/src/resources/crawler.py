import asyncio
from aiohttp import ClientSession
from fastapi import APIRouter
from fastapi.responses import JSONResponse


from src.models import LocalSession
from src.models.scorpion import Warranty, LogSystem
from src.utils.urls import URL_MAPPING
from src.core.crawler import Crawler
from src.utils import create_dates, create_dates_from_range
from src.schemas import GetFlowPayload, get_flow_responses

from src.exceptions import *


router = APIRouter()


@router.post("/get-flow", responses=get_flow_responses)
async def get_flow(payload: GetFlowPayload):
    try:
        if payload.dates:
            dates = create_dates_from_range(payload.dates)
        else:
            dates = create_dates()

        async with ClientSession() as session:
            crawler = Crawler(session, url_mapping=URL_MAPPING)
            await crawler.login(payload.document_number, payload.login, payload.password)
            tasks = list()
            for date in dates:
                tasks.append(asyncio.ensure_future(crawler.get_flow(date)))
            flows = await asyncio.gather(*tasks)
        return JSONResponse(status_code=200, content=dict(message="SUCCESS", flows=flows))
    except LoginInvalidoException:
        return JSONResponse(status_code=401, content=dict(message="INVALID_PASSWORD"))
    except CNPJInvalidoException:
        return JSONResponse(status_code=401, content=dict(message="INVALID_CNPJ"))
    except InstabilidadeNoAdquirente:
        return JSONResponse(status_code=500, content=dict(message="ERROR_ADQ"))
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
