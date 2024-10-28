from fastapi import FastAPI
from app.routes.comercializacao import router as comercializacao_router
from app.routes.importacao import router as importacao_router
from app.routes.exportacao import router as exportacao_router
from app.routes.producao import router as producao_router
from app.routes.home import router as home_router
from app.routes.processamento import router as processamento_router


app = FastAPI()

# Incluindo as rotas com include_router, agrupando as rotas de produção, processamento, importação e exportação
app.include_router(comercializacao_router)
app.include_router(importacao_router)
app.include_router(exportacao_router)
app.include_router(home_router)
app.include_router(producao_router)
app.include_router(processamento_router)
