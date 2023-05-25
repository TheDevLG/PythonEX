import pytest
from email import gerador_email


def testeEmail():
    assert gerador_email("Carlos Souza Silva") == "css@empresa.com.br"
    assert gerador_email("Maria da Silva Castro") == "msc@empresa.com.br"
    assert gerador_email("João dos Santos Meira") == "jsm@empresa.com.br"
    assert gerador_email("Antônio dos Santos Cardoso") == "asc@empresa.com.br"
