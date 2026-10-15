from model.pessoa import Pessoa
from datetime import date
from model.excecoes import PacienteMenorDeIdadeException

class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        super().__init__(nome, celular, cpf)
        self._data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self._data_nascimento

    def is_maior_de_idade(self) -> bool:
        hoje = date.today()
        idade = hoje.year - self._data_nascimento.year - ((hoje.month, hoje.day) < (self._data_nascimento.month, self._data_nascimento.day))
        return idade >= 18

    def validar_independencia(self):
        if not self.is_maior_de_idade():
            raise PacienteMenorDeIdadeException("Pacientes menores de 18 anos não podem realizar atendimentos sozinhos.")

    def __str__(self):
        base_str = super().__str__()
        return base_str.replace(")", f", data_nascimento={self._data_nascimento})")