import tkinter as tk
from agenda import Agenda

class AgendaGUI:
    def __init__(self, master):
        self.master = master
        self.agenda = Agenda()

        self.label_nome = tk.Label(master, text='Nome:')
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)

        self.label_telefone = tk.Label(master, text='Telefone:')
        self.label_telefone.grid(row=1, column=0)

        self.entry_telefone = tk.Entry(master)
        self.entry_telefone.grid(row=1, column=1)

        self.label_email = tk.Label(master, text='E-mail:')
        self.label_email.grid(row=2, column=0)

        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=2, column=1)

        self.button_criar = tk.Button(master, text='Criar', command=self.criar_contato)
        self.button_criar.grid(row=3, column=0)

        self.button_pesquisar = tk.Button(master, text='Pesquisar', command=self.pesquisar_contato)
        self.button_pesquisar.grid(row=3, column=1)

        self.button_atualizar = tk.Button(master, text='Atualizar', command=self.atualizar_contato)
        self.button_atualizar.grid(row=4, column=0)

        self.button_apagar = tk.Button(master, text='Apagar', command=self.apagar_contato)
        self.button_apagar.grid(row=4, column=1)

        self.text_output = tk.Text(master, height=10, width=30)
        self.text_output.grid(row=5, column=0, columnspan=2)


    def criar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        self.agenda.adicionar_contato(nome, telefone, email)

    def __str__(self) -> str:
        return f'Nome: {self.entry_nome}, Telefone: {self.entry_telefone}, Email: {self.entry_email}'    
        

    def pesquisar_contato(self):
        nome = self.entry_nome.get()
        contato = self.agenda.buscar_contato(nome)
        if contato is None:
            self.text_output.insert(tk.END, 'Contato não encontrado.\n\n')
        else:
            self.text_output.insert(tk.END, 'Contato encontrado:\n{}\n\n'.format(str(contato)))

    def atualizar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        contato = self.agenda.atualizar_contato(nome, telefone, email)
        if contato is None:
            self.text_output.insert(tk.END, 'Contato não encontrado.\n\n')
        else:
            self.text_output.insert(tk.END, 'Contato atualizado:\n{}\n\n'.format(str(contato)))

    def apagar_contato(self):
        nome = self.entry_nome.get()
        contato = self.agenda.remover_contato(nome)
        if contato is None:
            self.text_output.insert(tk.END, 'Contato não encontrado.\n\n')
        else:
            self.text_output.insert(tk.END, 'Contato apagado:\n{}\n\n'.format(str(contato)))

root = tk.Tk()
agenda_gui = AgendaGUI(root)
root.mainloop()
