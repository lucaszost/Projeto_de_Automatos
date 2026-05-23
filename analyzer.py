import re
from config import *
import validators
import stats

def inspecao(arquivo):
    numeroLinhas = 0
    with open(arquivo, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                numeroLinhas += 1
    return numeroLinhas

def verificaTipo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        for line in file:
            linha = line.strip()
            if not linha:
                continue
            if re.search(REGEX_CHAT, linha):
                return "Chat"
            elif re.search(REGEX_LOG, linha):
                return "Log"
            elif arquivo.suffix == '.csv':
                return "CSV"
            else:
                return "Texto Livre"
    return "Desconhecido"

def adicionarAtributo(dadosLinha, tipo, valor, classificacao):
    dadosLinha[tipo] = {
        "valor": valor,
        "classificacao": classificacao
    }

def validarCSV(arquivo):
    inconsistencias = []
    if arquivo.suffix != '.csv':
        return inconsistencias

    with open(arquivo, 'r', encoding='utf-8') as file:
        quantidadeColunas = None
        for numeroLinha, line in enumerate(file, start=1):
            linha = line.strip()
            if not linha:
                continue
            
            colunas = linha.split(';')
            if quantidadeColunas is None:
                quantidadeColunas = len(colunas)

            # quantidade inconsistente
            if len(colunas) != quantidadeColunas:
                inconsistencias.append({
                    "linha": numeroLinha,
                    "problema": "Quantidade de colunas inconsistente",
                    "quantidade_colunas": len(colunas),
                    "esperado": quantidadeColunas,
                    "conteudo": linha
                })

            # campos vazios
            for indice, coluna in enumerate(colunas):
                if coluna.strip() == '':
                    inconsistencias.append({
                        "linha": numeroLinha,
                        "coluna": indice,
                        "problema": "Campo vazio",
                        "conteudo": linha
                    })
    return inconsistencias

def extrairOcorrencias(arquivo):
    ocorrencias = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        for numeroLinha, line in enumerate(file, start=1):
            linhaOriginal = line.strip()
            if not linhaOriginal:
                continue
            
            dadosLinha = {}

            # data e hora
            datasHoras = re.findall(REGEX_DATA_HORA, linhaOriginal)
            for dataHora in datasHoras:
                adicionarAtributo(dadosLinha, "data_hora", dataHora, "valido")
                stats.estatisticas["datas_horas"]["total"] += 1
                stats.atualizarEstatisticaArquivo("datas_horas", arquivo)

            # emails
            emails = re.findall(REGEX_EMAIL_INVALIDO, linhaOriginal)
            for email in emails:
                classificacao = "valido" if validators.validarEmail(email) else "invalido"
                adicionarAtributo(dadosLinha, "email", email, classificacao)
                stats.estatisticas["emails"]["total"] += 1
                stats.estatisticas["emails"][f"{classificacao}s"] += 1
                stats.atualizarEstatisticaArquivo("emails", arquivo)

            # telefones
            telefones = re.findall(REGEX_TELEFONE_INVALIDO, linhaOriginal)
            for telefone in telefones:
                classificacao = "valido" if validators.validarTelefone(telefone) else "invalido"
                adicionarAtributo(dadosLinha, "telefone", telefone, classificacao)
                stats.estatisticas["telefones"]["total"] += 1
                stats.estatisticas["telefones"][f"{classificacao}s"] += 1
                stats.atualizarEstatisticaArquivo("telefones", arquivo)

            # cpfs
            cpfs = re.findall(REGEX_CPF_INVALIDO, linhaOriginal)
            for cpf in cpfs:
                classificacao = "valido" if validators.validarCPF(cpf) else "invalido"
                adicionarAtributo(dadosLinha, "cpf", cpf, classificacao)
                stats.estatisticas["cpfs"]["total"] += 1
                stats.estatisticas["cpfs"][f"{classificacao}s"] += 1
                stats.atualizarEstatisticaArquivo("cpfs", arquivo)

            # urls
            urls = re.findall(REGEX_URL_INVALIDA, linhaOriginal)
            for url in urls:
                classificacao = "valido" if validators.validarURL(url) else "invalido"
                adicionarAtributo(dadosLinha, "url", url, classificacao)
                stats.estatisticas["urls"]["total"] += 1
                stats.estatisticas["urls"][f"{classificacao}s"] += 1
                stats.atualizarEstatisticaArquivo("urls", arquivo)

            # datas
            datas = re.findall(REGEX_DATA, linhaOriginal)
            for data in datas:
                adicionarAtributo(dadosLinha, "data", data, "valido")
                stats.estatisticas["datas"]["total"] += 1
                stats.atualizarEstatisticaArquivo("datas", arquivo)

            # horas
            horas = re.findall(REGEX_HORA, linhaOriginal)
            for hora in horas:
                adicionarAtributo(dadosLinha, "hora", hora, "valido")
                stats.estatisticas["horas"]["total"] += 1
                stats.atualizarEstatisticaArquivo("horas", arquivo)

            # valores monetarios
            valores = re.findall(REGEX_DINHEIRO, linhaOriginal)
            for valor in valores:
                adicionarAtributo(dadosLinha, "valor_monetario", valor, "valido")
                stats.estatisticas["valores_monetarios"]["total"] += 1
                stats.atualizarEstatisticaArquivo("valores_monetarios", arquivo)

            # nomes
            nomes = re.findall(REGEX_NOME, linhaOriginal)
            for nome in nomes:
                adicionarAtributo(dadosLinha, "nome", nome, "valido")
                stats.estatisticas["nomes"]["total"] += 1
                stats.atualizarEstatisticaArquivo("nomes", arquivo)

            # adicionar linha agrupada se encontrou algo
            if dadosLinha:
                ocorrencias.append({
                    "linha": numeroLinha,
                    "arquivo_origem": arquivo.name,
                    "conteudo": linhaOriginal,
                    "dados": dadosLinha
                })

    return ocorrencias

def mostrarAmostra(arquivo, quantidade=5):
    amostra = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        for numeroLinha, line in enumerate(file, start=1):
            linha = line.strip()
            if not linha:
                continue
            amostra.append({
                "linha": numeroLinha,
                "conteudo": linha
            })
            if len(amostra) == quantidade:
                break
    return amostra
