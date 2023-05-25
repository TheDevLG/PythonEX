def gerador_email(nome):
    """
    Gera o e-mail de um funcionário com base no seu nome.
    
    Parameters:
        nome (str): nome completo do funcionário
        
    Returns:
        str: e-mail do funcionário na forma abreviada
             (ex: "css@empresa.com.br" para "Carlos Souza Silva")
    """
    partes_nome = nome.lower().split()
    iniciais = "".join([parte[0] for parte in partes_nome])
    email = iniciais + "@empresa.com.br"
    return email


def gerador_arquivo_emails(arquivo_entrada, arquivo_saida):
    """
    Lê o arquivo de entrada com os nomes dos funcionários e gera um arquivo de saída com
    os e-mails dos funcionários ordenados por nome.
    
    Parameters:
        arquivo_entrada (str): caminho do arquivo de entrada com os nomes dos funcionários
        arquivo_saida (str): caminho do arquivo de saída para os e-mails dos funcionários
    """
    try:
        # Lê os nomes dos funcionários do arquivo de entrada
        with open(arquivo_entrada, "r") as f:
            nomes_funcionarios = [linha.strip() for linha in f if linha.strip()]

        # Gera os e-mails dos funcionários
        emails_funcionarios = [gerador_email(nome) for nome in nomes_funcionarios]

        # Ordena os funcionários por nome
        funcionarios_ordenados = sorted(zip(nomes_funcionarios, emails_funcionarios))

        # Escreve os funcionários e seus e-mails ordenados no arquivo de saída
        with open(arquivo_saida, "w") as f:
            f.write("\n".format("NOME", "E-MAIL"))
            for nome, email in funcionarios_ordenados:
                f.write("\n".format(nome, email))

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Erro: ", e)



