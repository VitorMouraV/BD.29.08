class Pessoa:
    def __init__(self):  # metodo construtor
        self.nome = ""
        self.telefone = ""
        self.endereco = ""

    # Metodos de acesso
    def getNome(self):
        return self.nome

    def gettelefone(self):
        return self.telefone

    def getendereco(self):
        return self.endereco

    def setNome(self, nome):
        self.nome = nome

    def setendereco(self, endereco):
        self.endereco = endereco

    def settelefone(self, telefone):
        self.telefone = telefone
        # cadastrar

    def cadastrar(self, nome, telefone, endereco):
        self.setNome(nome)
        self.settelefone(telefone)
        self.setendereco(endereco)
        # Consultar Pessoa

    def consultarTudo(self):
        return "Nome: {}\nTelefone: {}\nEndereco: {}".format(self.getNome(), self.gettelefone(), self.getendereco())
