from fastapi import APIRouter
from app.services.dados_embrapa import obter_dados3

router = APIRouter()

@router.get('/producao1')
async def obter_producao():
    data = obter_dados3('producao1')
    return data