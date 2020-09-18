from typing import Tuple, Dict, Union

from aiohttp import ClientSession

from src.core.base import BaseCrawler
from src.schemas import FlowItem


class Crawler(BaseCrawler):

    def __init__(self, session: ClientSession, url_mapping: Dict):
        super().__init__(session, url_mapping)

    async def login(self, document_number: str, login: str, password: str):
        raise NotImplementedError("A lógica de autenticação precisa ser implementada.")

    async def get_flow(self, period: Tuple[str, str]) -> FlowItem:
        raise NotImplementedError("A lógica de extração dos dados precisa ser implementada.")

