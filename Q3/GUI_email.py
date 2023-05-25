import tkinter as tk


def gerador_email(nome):
    """
    Gera o e-mail de um funcionário com base no seu nome.
    
    Parameters:
        nome (str): nome completo do funcionário
        
    Returns:
        str: e-mail do funcionário na forma abreviada (iniciais)
             (ex: "css@empresa.com.br" para "Carlos Souza Silva")
    """
    partes_nome = nome.lower().split()
    iniciais = "".join([parte[0] for parte in partes_nome])
    email = iniciais + "@empresa.com.br"
    return email


def gerador_emails():
    """
    Lê o nome digitado na caixa de texto e gera o e-mail correspondente.
    Exibe o e-mail na caixa de texto de resultado.
    
    Returns:
        None
    """
    nome = entrada.get()
    email = gerador_email(nome)
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, email)


# Janela principal
janela = tk.Tk()
janela.title("Gerador de E-mails")

# Caixa de texto para entrada do nome
texto_nome = tk.Label(janela, text="Digite o nome do funcionário:")
texto_nome.pack()
entrada = tk.Entry(janela)
entrada.pack()

# Botão para gerar o e-mail
botao = tk.Button(janela, text="Gerar e-mail", command=gerador_emails)
botao.pack()

# Caixa de texto para exibição do resultado
texto_resultado = tk.Label(janela, text="E-mail gerado:")
texto_resultado.pack()
resultado = tk.Text(janela, height=1)
resultado.pack()


janela.mainloop()
