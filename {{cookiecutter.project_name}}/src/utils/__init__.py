import re
from typing import List, Tuple

from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY
from datetime import timedelta, datetime


MASCARA_CNPJ = re.compile(r'\D')
MASCARA_DATA = "%d/%m/%Y"


def create_date_tuple(date: datetime) -> Tuple[str, str]:
    """
    Cria uma tupla contendo o primeiro e ultimo dia do mes da data recebida
    :param date: data
    :return: Tupla com primeiro e ultimo dia do mes
    """
    start_date = date - relativedelta(days=date.day - 1)
    return (
        start_date.strftime(MASCARA_DATA),
        ((start_date + relativedelta(months=1)) - timedelta(days=1)).strftime(MASCARA_DATA)
    )


def create_dates_from_range(input_dates: List[str]) -> List[Tuple[str, str]]:
    """
    Normaliza o periodo de busca customizado
    :param input_dates: Relação de datas para pesquisa customizada
    :return: Lista contendo as tuplas de data inicial e final para cada mês da pesquisa
    """
    dates = list()

    for date in input_dates:
        date = datetime.strptime(date, "%d-%m-%Y")
        dates.append(create_date_tuple(date))
    return dates


def create_dates(interval: int = 12) -> List[Tuple[str, str]]:
    """
    Gera uma lista contendo uma tupla com a data inicial e final para cada mês
    dentro do intervalo especificado.
    :param interval: Quantidade de meses que deve ser gerados a partir da data
    atual

    :return: Lista contendo as tuplas de data inicial e final para cada mês da pesquisa
    """
    today = datetime.today()

    # Calcula o primeiro dia do mês da data inicial
    start_date = datetime.today() - relativedelta(months=interval, days=today.day - 1)

    # Listas que serão utilizadas para armazenar as datas
    dates = list()
    for initial_date in rrule(freq=MONTHLY, count=interval, dtstart=start_date):
        dates.append(create_date_tuple(initial_date))
    return dates


def comparar_cnpj(cnpj_site: str, cnpj_cadastro: str) -> bool:
    """
    Compara dois CNPJs

    Remove qualquer caractere não numérico do cnpj do site e de cadastro antes da comparação
    para garantir a consistencia na checagem.

    :param cnpj_site: Numero do CNPJ capturado no site do parceiro
    :param cnpj_cadastro: Numero do CNPJ cadastrado no sistema
    :return: True se iguais
    """
    cnpj_cadastro = f"{re.sub(MASCARA_CNPJ, '', cnpj_cadastro):>014s}"
    cnpj_site = f"{re.sub(MASCARA_CNPJ, '', cnpj_site):>014s}"
    return cnpj_site == cnpj_cadastro


def formatar_valor(valor: str) -> float:
    valor = re.sub(r"\.", "", valor)
    valor = float(re.sub(r",", ".", valor))
    return valor
