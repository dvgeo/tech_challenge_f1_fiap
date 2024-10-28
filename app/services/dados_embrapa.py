from app.scraper import get_table_data,get_table_data2#, get_table_data3

# Organiza URLs em um dicionário para cada tipo de dado (produção, processamento, comercialização).
'''URLS = {
    'producao': 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02',
    'processamento_viniferas': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03',
    'processamento_americanas': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03',
    'processamento_uvas':'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03',
    'processamento_sem_classificacao':'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03',
    'comercializacao':'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
}'''

URLS = {
    'producao': './html/producao.html',
    'processamento_viniferas': './html/processamento_vinifera.html',
    'processamento_americanas': './html/processamento_americanas_hibridas.html',
    'processamento_uvas':'./html/processamento_uvas.html',
    'processamento_sem_classificacao':'./html/processamento_sem_classificacao.html',
    #'comercializacao':'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
}


# Organiza URLs em um dicionário para cada tipo de dado (importação e exportação).



URLS2 = {
    'importacao_vinhos': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05',
    'importacao_espumantes': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05',
    'importacao_uvas_frescas': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05',
    'importacao_uvas_passas': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05',
    'importacao_suco_uva': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05',
    'exportacao_vinhos': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06',
    'exportacao_espumantes': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06',
    'exportacao_uvas_frescas': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06',
    'exportacao_suco_uva': 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06',  
}



def obter_dados(tipo: str) -> dict:
    """Obtém dados a partir do tipo especificado."""
    url = URLS.get(tipo) # Pega a URL correspondente ao tipo fornecido
    if not url: # Se o tipo for inválido, lança um erro
        raise ValueError(f"Tipo '{tipo}' não encontrado.")
    return get_table_data(url) # Faz o scraping executando a função e retorna os dados 

def obter_dados2(tipo: str) -> dict:
    """Obtém dados a partir do tipo especificado."""
    url = URLS2.get(tipo)  # Pega a URL correspondente ao tipo fornecido
    if not url: # Se o tipo for inválido, lança um erro
        raise ValueError(f"Tipo '{tipo}' não encontrado.")
    return get_table_data2(url) # Faz o scraping execut''ando a função e retorna os dados
