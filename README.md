# Projeto-de-Automatos

Projeto desenvolvido para a disciplina de Linguagens Formais e Autômatos utilizando Expressões Regulares (Regex) para reconhecimento, extração, validação e estruturação de dados presentes em arquivos semi-estruturados e desorganizados.

O sistema realiza análise textual automatizada em múltiplos formatos de arquivos, identificando padrões sintáticos relevantes, classificando conteúdos e exportando os resultados em formato JSON estruturado.

---

# Objetivo

O objetivo do projeto é implementar um sistema de inspeção textual baseado em Expressões Regulares capaz de:

* realizar leitura automatizada de arquivos;
* identificar o tipo estrutural do conteúdo;
* extrair padrões textuais;
* validar cadeias utilizando Regex;
* detectar inconsistências estruturais;
* organizar dados em formato estruturado;
* gerar arquivos JSON;
* produzir estatísticas quantitativas dos dados encontrados.


---

# Estrutura do Projeto

```txt
Projeto-de-automatos/
│
├── Artigo/
|   └── artigo.pdf
|
├── assets/
│   ├── 01_atendimentos_bagunçados.txt
│   ├── 02_logs_mistos.log
│   ├── 03_mensagens_chat.txt
│   └── 04_exportacao_suja.csv
│
├── resultados_json/
│   ├── 01_atendimentos_bagunçados.json
|   ├── 02_logs_mistos.json
|   ├── 03_mensagens_chat.json
|   ├── 04_exportacao_suja.json
|   └── estatisticas.json
|
├── README.md
├── analyzer.py
├── config.py
├── main.py
├── stats.py
└── validators.py
```

---

# Arquivos Obrigatórios

O sistema processa obrigatoriamente os seguintes arquivos:

| Arquivo                          | Tipo Esperado     |
| -------------------------------- | ----------------- |
| `01_atendimentos_bagunçados.txt` | Texto Livre       |
| `02_logs_mistos.log`             | Logs              |
| `03_mensagens_chat.txt`          | Chat              |
| `04_exportacao_suja.csv`         | CSV inconsistente |

---

# Arquitetura Geral do Sistema

O sistema é dividido em etapas independentes de processamento:

1. leitura dos arquivos;
2. contagem de linhas válidas;
3. identificação do tipo de conteúdo;
4. extração de padrões textuais;
5. validação estrutural;
6. organização das ocorrências;
7. validação estrutural de CSV;
8. geração de estatísticas;
9. exportação dos resultados em JSON.

---

# Expressões Regulares Utilizadas

O projeto utiliza Regex para reconhecimento de cadeias textuais específicas.

| Tipo               | Variável                  |
| ------------------ | ------------------------- |
| Chat               | `REGEX_CHAT`              |
| Logs               | `REGEX_LOG`               |
| Datas              | `REGEX_DATA`              |
| Horas              | `REGEX_HORA`              |
| Data/Hora          | `REGEX_DATA_HORA`         |
| E-mail válido      | `REGEX_EMAIL`             |
| E-mail genérico    | `REGEX_EMAIL_INVALIDO`    |
| Telefone válido    | `REGEX_TELEFONE`          |
| Telefone genérico  | `REGEX_TELEFONE_INVALIDO` |
| CPF válido         | `REGEX_CPF`               |
| CPF genérico       | `REGEX_CPF_INVALIDO`      |
| URL válida         | `REGEX_URL`               |
| URL genérica       | `REGEX_URL_INVALIDA`      |
| Valores monetários | `REGEX_DINHEIRO`          |
| Nome próprio       | `REGEX_NOME`              |

---

# Fluxo de Execução

A função principal responsável pela execução do sistema é:

```python
def inspecionar()
```

Ela controla todo o pipeline de processamento.

---

# Leitura e Inspeção de Arquivos

## Função

```python
def inspecao(arquivo)
```


Executa a leitura sequencial do arquivo utilizando streaming de linhas.

## Responsabilidades

* abrir o arquivo utilizando UTF-8;
* percorrer todas as linhas;
* ignorar linhas vazias;
* contabilizar apenas linhas válidas;
* retornar o total de linhas úteis.

## Retorno

```python
numeroLinhas
```

## Complexidade

```txt
O(n)
```

Onde `n` representa a quantidade de linhas do arquivo.

---

# Identificação do Tipo do Conteúdo

## Função

```python
def verificaTipo(arquivo)
```


Classificar semanticamente o conteúdo do arquivo utilizando heurísticas baseadas em Regex e extensão do arquivo.

## Regras de Classificação

### Chat

Identificado por padrões contendo:

```txt
[dd/mm/yyyy hh:mm]
```

### Log

Identificado por palavras-chave:

```txt
[INFO]
[ERROR]
[WARN]
```

### CSV

Identificado pela extensão:

```txt
.csv
```

### Texto Livre

Conteúdo sem padrão estrutural identificado.

## Retorno

| Tipo        | Descrição                  |
| ----------- | -------------------------- |
| Chat        | Conversas estruturadas     |
| Log         | Logs operacionais          |
| CSV         | Dados tabulares            |
| Texto Livre | Texto sem estrutura rígida |

---

# Extração de Ocorrências

## Função

```python
def extrairOcorrencias(arquivo)
```


Executar mineração textual baseada em Expressões Regulares para extração de padrões estruturados.

## Processo Interno

A função:

1. percorre todas as linhas do arquivo;
2. aplica múltiplas Regex;
3. identifica padrões válidos e inválidos;
4. classifica os resultados;
5. organiza os dados em estrutura JSON;
6. atualiza estatísticas globais.

## Padrões Extraídos

* e-mails;
* telefones;
* CPFs;
* URLs;
* datas;
* horários;
* datas e horários;
* valores monetários;
* nomes próprios.

---

# Sistema de Validação Estrutural

## Funções

```python
def validarEmail(email)
def validarTelefone(telefone)
def validarCPF(cpf)
def validarURL(url)
```


Executar validação sintática utilizando:

```python
re.fullmatch()
```

## Estratégia de Validação

O sistema utiliza duas etapas:

### 1. Captura Genérica

Regex mais permissiva para localizar padrões potencialmente inválidos.

### 2. Validação Estrutural

Regex restritiva para determinar:

* válido;
* inválido.

---

# Organização das Ocorrências

## Função

```python
def adicionarAtributo()
```

Normalizar e estruturar os padrões encontrados em formato JSON.

## Estrutura Produzida

```json
{
    "email": {
        "valor": "usuario@email.com",
        "classificacao": "valido"
    }
}
```

---

# Estruturação das Linhas Processadas

Cada linha processada é agrupada em uma estrutura organizada contendo:

```json
{
    "linha": 10,
    "arquivo_origem": "arquivo.csv",
    "conteudo": "linha original",
    "dados": {}
}
```

## Campos

| Campo            | Descrição              |
| ---------------- | ---------------------- |
| `linha`          | Número da linha        |
| `arquivo_origem` | Nome do arquivo        |
| `conteudo`       | Conteúdo textual bruto |
| `dados`          | Padrões extraídos      |

---

# Validação Estrutural de CSV

## Função

```python
def validarCSV(arquivo)
```


Identificar inconsistências estruturais em arquivos CSV delimitados por `;`.

## Verificações Implementadas

### Quantidade de Colunas

Verifica se todas as linhas possuem a mesma quantidade de colunas da linha inicial.

### Campos Vazios

Detecta colunas vazias ou ausentes.

## Estrutura das Inconsistências

```json
{
    "linha": 8,
    "problema": "Campo vazio",
    "coluna": 4
}
```

---

# Sistema de Estatísticas

## Estrutura Global

```python
estatisticas = {}
```


Armazenar métricas quantitativas globais durante o processamento.

## Informações Coletadas

* total de ocorrências;
* válidos;
* inválidos;
* distribuição por arquivo;
* inconsistências CSV.

---

# Atualização de Estatísticas

## Função

```python
def atualizarEstatisticaArquivo()
```

## Objetivo Técnico

Incrementar dinamicamente os contadores estatísticos por categoria e por arquivo processado.

---

# Amostragem de Conteúdo

## Função

```python
def mostrarAmostra()
```

## Objetivo Técnico

Produzir uma visualização resumida do conteúdo do arquivo.

## Estratégia

* leitura parcial;
* ignorar linhas vazias;
* limitar quantidade de exemplos;
* preservar número original da linha.

## Estrutura Gerada

```json
{
    "linha": 1,
    "conteudo": "texto da linha"
}
```

---

# Geração de JSON Individual

## Função

```python
def gerarJsonArquivo()
```

## Objetivo Técnico

Exportar os dados processados para arquivos JSON estruturados.

## Dados Exportados

Cada JSON contém:

* nome do arquivo;
* tipo do conteúdo;
* número de linhas;
* amostras;
* ocorrências agrupadas;
* inconsistências CSV.

## Local de Saída

```txt
./resultados_json/
```

---

# Geração de Estatísticas Gerais

## Função

```python
def gerarEstatisticas()
```

## Objetivo Técnico

Persistir estatísticas globais em formato JSON.

## Arquivo Gerado

```txt
resultados_json/estatisticas.json
```

---

# Exemplo de Estrutura JSON Gerada

```json
{
    "arquivo": "04_exportacao_suja.csv",
    "tipo_conteudo": "CSV",
    "numero_linhas": 120,
    "amostra": [],
    "ocorrencias_agrupadas": [],
    "inconsistencias_csv": []
}
```

---

# Requisitos Atendidos pelo Sistema

| Requisito                        | Status |
| -------------------------------- | ------ |
| Ler todos os arquivos fornecidos | \(\checkmark \)      |
| Contabilizar linhas              | \(\checkmark \)      |
| Identificar tipo do conteúdo     | \(\checkmark \)      |
| Detectar Chat                    | \(\checkmark \)      |
| Detectar Logs                    | \(\checkmark \)      |
| Detectar CSV                     | \(\checkmark \)      |
| Detectar Texto Livre             | \(\checkmark \)      |
| Apresentar amostras              | \(\checkmark \)      |
| Extrair padrões textuais         | \(\checkmark \)      |
| Validar padrões                  | \(\checkmark \)      |
| Gerar JSON                       | \(\checkmark \)      |
| Gerar estatísticas               | \(\checkmark \)      |
| Detectar inconsistências CSV     | \(\checkmark \)      |

---

# Como Executar

## Requisitos

```txt
Python 3.10+
```

---

## Execução

### 1. Inserir arquivos

Colocar os arquivos dentro de:

```txt
./assets/
```

### 2. Executar

```bash
python main.py
```

---

# Saídas Produzidas

## Terminal

O sistema exibe:

* nome do arquivo;
* quantidade de linhas;
* tipo identificado;
* amostras;
* total de ocorrências;
* estatísticas gerais.

---

## JSONs Individuais

Gerados automaticamente em:

```txt
./resultados_json/
```

---

# Tecnologias Utilizadas

| Tecnologia    | Finalidade                |
| ------------- | ------------------------- |
| Python        | Linguagem principal       |
| Regex (`re`)  | Reconhecimento de padrões |
| JSON (`json`) | Estruturação dos dados    |
| Pathlib       | Manipulação de caminhos   |

---

# Conceitos Aplicados

* Linguagens Formais;
* Expressões Regulares;
* Reconhecimento Léxico;
* Validação Sintática;
* Processamento de Texto;
* Estruturação de Dados;
* Mineração Textual;
* Análise Semi-Estruturada.

---

# Limitações do Sistema

* validação apenas estrutural;
* CPF não possui verificação de dígitos verificadores;
* URLs não são verificadas semanticamente;
* não há normalização de encoding;
* não existe parser CSV formal.
* Casos de invalidez: user=975lc7@hotmail.com ou email=@outlook.com
