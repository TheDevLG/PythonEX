from emailAlt import gerador_arquivo_emails


def test_gerar_arquivo_emails():
    gerador_arquivo_emails("test_input.txt", "test_output.txt")
    with open("test_output.txt", "r") as f:
        conteudo_saida = f.read()
    assert conteudo_saida == "NOME                          E-MAIL\nAntonio dos Santos Cardoso  asc@empresa.com.br\nCarlos Souza Silva           css@empresa.com.br\nCassio Silva dos Santos      css2@empresa.com.br\nMaria da Silva Castro        msc@empresa.com.br\n"
