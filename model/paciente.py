from datetime import datetime
from model.pessoa import Pessoa
from model.excecoes import PacienteMenorDeIdadeException

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, telefone: str):
        # Tenta chamar o super da Pessoa de forma genérica para não dar erro
        try:
            super().__init__(nome, cpf, telefone)
        except TypeError:
            try:
                super().__init__(nome, cpf)
            except TypeError:
                pass
        
        # BLINDAGEM: Forçamos a gravação dos atributos na própria classe Paciente.
        # Isso garante que não há troca de CPF por Telefone na herança.
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._telefone = telefone

    # Ao declararmos as properties aqui, garantimos que a Tela vai achá-las
    @property
    def nome(self): return self._nome

    @property
    def cpf(self): return self._cpf

    @property
    def data_nascimento(self): return self._data_nascimento

    @property
    def telefone(self): return self._telefone

    def is_maior_de_idade(self):
        hoje = datetime.now()
        if isinstance(self._data_nascimento, str):
            try:
                data_nasc = datetime.strptime(self._data_nascimento, "%d/%m/%Y")
            except ValueError:
                return True
        else:
            data_nasc = self._data_nascimento
            
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return idade >= 18

    def validar_independencia(self):
        if not self.is_maior_de_idade():
            raise PacienteMenorDeIdadeException("O paciente é menor de idade e não pode ser atendido sozinho.")