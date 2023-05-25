def gerador_email(nome):
    """
    Gera o e-mail de um funcionário com base no seu nome.
    
    Parameters:
        nome (str): nome completo do funcionário
        
    Returns:
        str: e-mail do funcionário na forma abreviada (iniciais)
             
    """
    partes_nome = nome.lower().split()
    iniciais = "".join([parte[0] for parte in partes_nome])
    email = iniciais + "@empresa.com.br"
    return email

# Testes práticos
print(gerador_email("Carlos Souza Silva"))  # css@empresa.com.br
print(gerador_email("Maria da Silva Castro"))  # msc@empresa.com.br
print(gerador_email("João dos Santos Meira"))  # jsm@empresa.com.br
print(gerador_email("Antônio dos Santos Cardoso"))  # asc@empresa.com.br
