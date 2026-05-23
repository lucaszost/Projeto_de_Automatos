import json
import config
import analyzer
import stats

def gerarJsonArquivo(arquivo, numeroLinhas, tipoArquivo, amostra, ocorrencias, inconsistenciasCSV):
    dados = {
        "arquivo": arquivo.name,
        "tipo_conteudo": tipoArquivo,
        "numero_linhas": numeroLinhas,
        "amostra": amostra,
        "ocorrencias_agrupadas": ocorrencias,
        "inconsistencias_csv": inconsistenciasCSV
    }

    nomeJson = arquivo.stem + ".json"
    caminhoJson = config.DIRETORIO_JSON / nomeJson

    with open(caminhoJson, 'w', encoding='utf-8') as jsonFile:
        json.dump(dados, jsonFile, ensure_ascii=False, indent=4)

    print(f"\nJSON gerado: {caminhoJson}")

def gerarEstatisticas():
    caminhoEstatisticas = config.DIRETORIO_JSON / "estatisticas.json"

    with open(caminhoEstatisticas, 'w', encoding='utf-8') as jsonFile:
        json.dump(stats.estatisticas, jsonFile, ensure_ascii=False, indent=4)

    print("\033[31m#\033[0m" * 180)
    print("\nESTATISTICAS GERAIS:\n")
    for tipo, dados in stats.estatisticas.items():
        print(tipo.upper())
        for chave, valor in dados.items():
            print(f"  {chave}: {valor}")
        print()

def inspecionar():
    # Cria pasta caso não exista
    config.DIRETORIO_JSON.mkdir(exist_ok=True)

    for nomeArquivo in config.ARQUIVOS_OBRIGATORIOS:
        arquivo = config.DIRETORIO_ASSETS / nomeArquivo

        if arquivo.exists() and arquivo.is_file():
            numeroLinhas = analyzer.inspecao(arquivo)
            tipoArquivo = analyzer.verificaTipo(arquivo)
            amostra = analyzer.mostrarAmostra(arquivo)
            ocorrencias = analyzer.extrairOcorrencias(arquivo)
            inconsistenciasCSV = analyzer.validarCSV(arquivo)

            if inconsistenciasCSV:
                stats.estatisticas["csv_inconsistente"]["total"] += len(inconsistenciasCSV)
                stats.estatisticas["csv_inconsistente"]["arquivos"][arquivo.name] = len(inconsistenciasCSV)

            print("\033[32m#\033[0m" * 180)
            print(f"ARQUIVO: {arquivo.name}")
            print(f"LINHAS: {numeroLinhas}")
            print(f"TIPO: {tipoArquivo}")
            print("\nAMOSTRA:\n")
            
            for item in amostra:
                print("-" * 150)
                print(f"[Linha {item['linha']}] {item['conteudo']}")
            
            print(f"\nTOTAL DE OCORRENCIAS: {len(ocorrencias)}")

            if ((numeroLinhas - len(ocorrencias)) > 0):            
                print(f"\nTOTAL DE OCORRENCIAS INVÁLIDAS: {numeroLinhas - len(ocorrencias)}")


            gerarJsonArquivo(arquivo, numeroLinhas, tipoArquivo, amostra, ocorrencias, inconsistenciasCSV)

        else:
            print(f"Arquivo nao encontrado: {nomeArquivo}")

    gerarEstatisticas()

if __name__ == '__main__':
    inspecionar()
