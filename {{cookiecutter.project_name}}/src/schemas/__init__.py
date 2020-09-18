"""
O esquemas devem extender a class BaseModel do pacote pydantic

e.g:
    from pydantic import BaseModel

    class User(BaseModel):
        id: int
        name: str

"""
import re

from typing import Optional, List
from pydantic import BaseModel, validator, Field


DATE_FORMAT = re.compile(r"(\d\d-){2}\d{4}")


class FlowItem(BaseModel):
    date: str
    flow: float


class Flow(BaseModel):
    message: str
    establishment_number: Optional[str]
    flows: List[FlowItem]

    class Config:
        schema_extra = {
            "example": {
                "message": "SUCCESS",
                "establishment_number": "123546",
                "flows": [
                    {
                        "date": "2020-01-01",
                        "flow": 1000.00
                    },
                    {
                        "date": "2020-02-01",
                        "flow": 650.00
                    }
                ]
            }
        }


class MessageResponse(BaseModel):
    message: str


class ValidateLoginPayload(BaseModel):
    document_number: str
    login: str
    password: str
    sipag: Optional[bool] = False

    class Config:
        schema_extra = {
            "example": {
                "login": "usuario@sistema.com",
                "password": "123mudar",
                "document_number": "12123123000132",
                "sigpag": True,
            }
        }


class GetFlowPayload(BaseModel):
    document_number: str
    login: str
    password: str
    dates: List[Optional[str]] = Field(description="Relação de datas para pesquisa")
    sipag: Optional[bool] = False

    @validator("dates")
    def check_content(cls, dates):
        for d in dates:
            if not re.fullmatch(DATE_FORMAT, d):
                raise ValueError("Invalid date format")
        return dates

    class Config:
        schema_extra = {
            "example": {
                "login": "usuario@sistema.com",
                "password": "123mudar",
                "document_number": "12123123000132",
                "sigpag": True,
                "dates": [
                    "01-01-2020", "16-03-2020"
                ]
            }
        }


get_flow_responses = {
        200: {"model": Flow, "description": "Success"},
        400: {
            "model": MessageResponse, "description": "CNPJ inválido",
            "content": {
                "application/json": {
                    "example": {"message": "INVALID_CNPJ"}
                }
            }
        },
        401: {
            "model": MessageResponse, "description": "Senha inválida",
            "content": {
                "application/json": {
                    "example": {"message": "INVALID_PASSWORD"}
                }
            }
        },
        502: {
            "model": MessageResponse, "description": "Erro no adquirente",
            "content": {
                "application/json": {
                    "example": {"message": "ERROR_ADQ"}
                }
            }
        },
        500: {
            "model": MessageResponse, "description": "Erro inesperado",
            "content": {
                "application/json": {
                    "example": {"message": "Unexpected error"}
                }
            }
        },
    }


validate_login_responses = {
    200: {
        "description": "Credenciais OK",
        "model": MessageResponse,
        "content": {
            "application/json": {
                "example": {"message": "SUCCESS"}
            }
        }
    },
    401: {
        "description": "Credenciais Inválidas",
        "model": MessageResponse,
        "content": {
            "application/json": {
                "example": {"message": "INVALID_PASSWORD|INVALID_CNPJ" }
            }
        }
    },
    500: {
        "description": "Erro inesperado",
        "model": MessageResponse,
        "content": {
            "application/json": {
                "example": {"message": "Some exception message"}
            }
        }
    },
    502: {
        "description": "Falha de comunicação com o adquirente",
        "model": MessageResponse,
        "content": {
            "application/json": {
                "example": {"message": "ERROR_ADQ"}
            }
        }
    }
}