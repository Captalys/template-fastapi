from typing import Tuple, Dict

from abc import ABC, abstractmethod
from aiohttp import ClientSession

from src.schemas import FlowItem


class BaseCrawler(ABC):

    def __init__(self, session: ClientSession, url_map: Dict):
        """
        Construtor da classe base.
        :param session: Sessao que sera utilizada durante toda a extracao de dados
        :param url_map: Mapeamento das urls que serão utilizadas durante a extracao.
        """
        self.session = session
        self.url_map = url_map

    @abstractmethod
    async def login(self, document_number: str, login: str, password: str) -> bool:
        """
        Efetua a autenticação na API do adquirente
        :param document_number: CNPJ para conferência
        :param login: Usuário de acesso ao site
        :param password: Senha do usuário
        :return: Caso todos os processos de autenticação sejam efetuados com sucesso True
        """
        pass

    @abstractmethod
    async def get_flow(self, period: Tuple[str, str]) -> FlowItem:
        """
        Este método é o que buscará os dados de fluxo e será executado de forma paralela
        :param session: Sessão autenticada do usuário
        :param period: Tupla contendo a data_inicial e data_final para pesquisa. Exemplo: ("2020-01-01", "2020-01-31")
        :return:
        """
        pass
