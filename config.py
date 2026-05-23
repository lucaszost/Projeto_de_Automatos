from pathlib import Path

# Configurações de Diretórios
DIRETORIO_ASSETS = Path('./assets/')
DIRETORIO_JSON = Path('./resultados_json/')

# arquivos para leitura
ARQUIVOS_OBRIGATORIOS = [
    '01_atendimentos_bagunçados.txt',
    '02_logs_mistos.log',
    '03_mensagens_chat.txt',
    '04_exportacao_suja.csv'
]

# Expressões Regulares (Regex)
REGEX_CHAT = r'^\[\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}(?::\d{2})?\]'
REGEX_LOG = r'\[INFO\]|\[ERROR\]|\[WARN\]'
REGEX_DATA = r'\d{2}/\d{2}/\d{4}'
REGEX_HORA = r'\d{2}:\d{2}(?::\d{2})?'
REGEX_DATA_HORA = r'\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}(?::\d{2})?'
REGEX_EMAIL = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
REGEX_EMAIL_INVALIDO = r'[^;\s@]+@[^;\s@]+'
REGEX_TELEFONE = r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}'
REGEX_TELEFONE_INVALIDO = r'\(?\d{2}\)?\s?\d{4,5}-?\d{3,4}'
REGEX_CPF = r'\b(?:\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})\b'
REGEX_CPF_INVALIDO = r'\b\d{3}(?:[.\-]?\d{3}){2}[.\-]?\d{1,2}\b'
REGEX_URL = r'https?://[^\s]+'
REGEX_URL_INVALIDA = r'(?:https?://[^\s;]+|www\.[^\s;]+)'
REGEX_DINHEIRO = r'R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}'
REGEX_NOME = r'\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+(?:\s[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+)+'
