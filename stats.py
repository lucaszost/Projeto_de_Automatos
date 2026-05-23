# Dicionário de estatísticas globais
estatisticas = {
    "emails": {"total": 0, "validos": 0, "invalidos": 0, "arquivos": {}},
    "telefones": {"total": 0, "validos": 0, "invalidos": 0, "arquivos": {}},
    "cpfs": {"total": 0, "validos": 0, "invalidos": 0, "arquivos": {}},
    "urls": {"total": 0, "validos": 0, "invalidos": 0, "arquivos": {}},
    "datas": {"total": 0, "arquivos": {}},
    "horas": {"total": 0, "arquivos": {}},
    "datas_horas": {"total": 0, "arquivos": {}},
    "valores_monetarios": {"total": 0, "arquivos": {}},
    "nomes": {"total": 0, "arquivos": {}},
    "csv_inconsistente": {"total": 0, "arquivos": {}}
}

def atualizarEstatisticaArquivo(tipo, arquivo):
    """Atualiza a contagem de um tipo específico dentro do registro de um arquivo"""
    nomeArquivo = arquivo.name
    if nomeArquivo not in estatisticas[tipo]["arquivos"]:
        estatisticas[tipo]["arquivos"][nomeArquivo] = 0
    estatisticas[tipo]["arquivos"][nomeArquivo] += 1
