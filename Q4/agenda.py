
class Contato:
    """
    Classe que representa um contato na agenda.

    Atributos:
        nome (str): nome do contato
        telefone (str): telefone do contato
        email (str): endereço de e-mail do contato
    """

    def __init__(self, nome, telefone, email):
        """
        Inicializa um novo objeto Contato.

        Parameters:
            nome (str): nome do contato
            telefone (str): telefone do contato
            email (str): endereço de e-mail do contato
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    """
    Classe que representa uma agenda de contatos.

    Atributos:
        contatos (list): lista de contatos da agenda
    """
    def __init__(self):
        """
        Inicializa uma nova agenda vazia.
        """
        self.contatos = []
        

    def adicionar_contato(self, nome, telefone, email):
        """
        Adiciona um novo contato na agenda.

        Parameters:
            contato (Contato): objeto Contato a ser adicionado na agenda
        """
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
       

    def buscar_contato(self, nome):
        """
        Pesquisa um contato na agenda pelo nome.

        Parameters:
            nome (str): nome do contato a ser pesquisado

        Returns:
            Contato: objeto Contato encontrado ou None caso o contato não seja encontrado
        """
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def atualizar_contato(self, nome, telefone, email):
        """
        Atualiza um contato na agenda.

        Parameters:
            nome (str): nome do contato a ser atualizado
            telefone (str): novo telefone do contato
            email (str): novo endereço de e-mail do contato
        """
        contato = self.buscar_contato(nome)
        if contato:
            contato.telefone = telefone
            contato.email = email
           
            return True
        return False

    def remover_contato(self, nome):
        """
        Remove um contato da agenda.

        Parameters:
            nome (str): nome do contato a ser removido
        """
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
        
            return True
        return False


