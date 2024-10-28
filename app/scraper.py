import requests # Para fazer a requisição HTTP
from bs4 import BeautifulSoup # Para processar o HTML da página

'''def get_table_data(url: str) -> dict:
    """Extrai dados de uma tabela específica da página HTML."""
    response = requests.get(url)  # Faz a requisição HTTP para a URL
    soup = BeautifulSoup(response.content, 'html.parser') # Converte o HTML para um objeto BeautifulSoup
    table = soup.find('table', class_='tb_base tb_dados')  # Encontra a tabela com a classe específica


    data = {} # Dicionário para armazenar os dados extraídos
    current_category = None # Variável para armazenar a categoria atual
    
    # Percorre cada linha da tabela
    for row in table.find_all('tr'):
        cells = row.find_all('td') # Coleta todas as células (<td>) de uma linha
        if len(cells) == 2: # Espera exatamente 2 células (nome e volume)
            if cells[0].get('class') == ['tb_item']: # Categoria principal
                current_category = cells[0].text.strip() # Remove espaços em branco do texto
                data[current_category] = {} # Cria um dicionário vazio para a nova categoria
            elif cells[0].get('class') == ['tb_subitem']: # Subcategoria 
                subcategory = cells[0].text.strip()
                volume = cells[1].text.strip() # Extrai a quantidade correspondente
                data[current_category][subcategory] = volume  # Adiciona a subcategoria e sua quantidade na categoria atual
    return data # Retorna o dicionário com as categorias e subcategorias'''

def get_table_data(file_path: str) -> dict:
    """Extrai dados de uma tabela específica de um arquivo HTML e organiza em um JSON estruturado."""
    
    # Abre o arquivo HTML local e lê seu conteúdo
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Cria o objeto BeautifulSoup com o conteúdo do HTML
    soup = BeautifulSoup(content, 'html.parser')

    # Encontra a tabela desejada
    table = soup.find('table', class_='tb_base tb_dados')

    data = {}  # Dicionário para armazenar os dados extraídos
    current_category = None  # Para rastrear a categoria principal
    total = None  # Variável para capturar o total ao final

    # Itera sobre cada linha da tabela
    for row in table.find_all('tr'):
        cells = row.find_all('td')  # Coleta todas as células da linha

        if len(cells) == 2:  # Espera exatamente 2 células por linha (nome e valor)
            cell_class = cells[0].get('class', [])

            if 'tb_item' in cell_class:  # Categoria principal
                current_category = cells[0].text.strip()  # Extrai o nome da categoria
                total_value = cells[1].text.strip()  # Extrai o valor total da categoria
                data[current_category] = {"total": total_value, "subitens": {}}  # Inicializa a estrutura da categoria

            elif 'tb_subitem' in cell_class and current_category:  # Subcategoria
                subcategory = cells[0].text.strip()  # Nome da subcategoria
                volume = cells[1].text.strip()  # Quantidade correspondente
                data[current_category]["subitens"][subcategory] = volume  # Adiciona o subitem à categoria atual

            elif not cell_class:  # Caso do "Total" geral
                total = cells[1].text.strip()

    # Adiciona o total geral no final, se existir
    if total:
        data["Total"] = total

    return data  # Retorna o dicionário estruturado

'''def get_table_data2(url: str) -> dict:
    """Extrai dados de uma tabela específica da página HTML."""
    response = requests.get(url) # Faz uma requisição GET para a URL fornecida e baixa o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser') # Faz uma requisição GET para a URL fornecida e baixa o conteúdo HTML

    table = soup.find('table', class_='tb_base tb_dados') # Busca a primeira tabela com a classe CSS 'tb_base tb_dados'
    data = {} # Um dicionário vazio é criado para armazenar os dados extraídos

    for row in table.find_all('tr')[1:]:  # Encontra todas as linhas da tabela (<tr>) e ignora a primeira linha, que é o cabeçalho.
        cells = row.find_all('td') # Para cada linha, encontra todas as células (<td>), que contêm os dados.
        country = cells[0].text.strip() # Extrai o nome do país (ou identificador) da primeira célula e remove espaços em branco com strip()
        quantity = cells[1].text.strip()  # Extrai a quantidade da segunda célula
        value = cells[2].text.strip()  # Extrai o valor da terceira célula.
        data[country] = {'quantidade': quantity, 'valor': value} # Cada país é uma chave no dicionário data O valor correspondente 
        # é um dicionário com a quantidade e o valor.
    return data'''

def get_table_data2(url: str) -> dict:
    """Extrai dados de uma tabela específica da página HTML."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Localiza a tabela com os dados desejados
    table = soup.find('table', class_='tb_base tb_dados')

    data = {"países": []}  # Lista para armazenar os dados dos países
    total_importacoes = {"quantidade": 0, "valor": 0}  # Para armazenar os totais

    # Itera sobre cada linha da tabela
    for row in table.find_all('tr'):
        cells = row.find_all('td')

        if len(cells) == 3:  # Espera exatamente 3 células: País, Quantidade, Valor
            pais = cells[0].text.strip()
            quantidade = cells[1].text.strip().replace('.', '')
            valor = cells[2].text.strip().replace('.', '')

            # Converte '-' em 0 para processamento
            quantidade = int(quantidade) if quantidade != '-' else 0
            valor = int(valor) if valor != '-' else 0

            # Verifica se é a linha do total
            if pais.lower() == "total":
                total_importacoes["quantidade"] = quantidade
                total_importacoes["valor"] = valor
            else:
                # Adiciona os dados do país na lista
                data["países"].append({
                    "país": pais,
                    "quantidade": quantidade,
                    "valor": valor
                })

    # Adiciona o total ao final do JSON
    data["total"] = total_importacoes

    return data