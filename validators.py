import re
from config import REGEX_EMAIL, REGEX_TELEFONE, REGEX_CPF, REGEX_URL

def validarEmail(email):
    return bool(re.fullmatch(REGEX_EMAIL, email))

def validarTelefone(telefone):
    return bool(re.fullmatch(REGEX_TELEFONE, telefone))

def validarCPF(cpf):
    return bool(re.fullmatch(REGEX_CPF, cpf))

def validarURL(url):
    return bool(re.fullmatch(REGEX_URL, url))
