from datetime import datetime
from model.pessoa import Pessoa
from model.excecoes import PacienteMenorDeIdadeException

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, telefone: str):
        try:
            super().__init__(nome, cpf, telefone)
        except TypeError:
            try:
                super().__init__(nome, cpf)
            except TypeError:
                pass
        
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._telefone = telefone

    @property
    def nome(self): return self._nome

    @property
    def cpf(self): return self._cpf

    @property
    def data_nascimento(self): return self._data_nascimento

    @property
    def telefone(self): return self._telefone

    def is_maior_de_idade(self, data_referencia=None):
        if data_referencia is None:
            referencia = datetime.now()
        elif isinstance(data_referencia, str):
            try:
                referencia = datetime.strptime(data_referencia, "%d/%m/%Y")
            except ValueError:
                referencia = datetime.now()
        else:
            referencia = data_referencia

        if isinstance(self._data_nascimento, str):
            try:
                data_nasc = datetime.strptime(self._data_nascimento, "%d/%m/%Y")
            except ValueError:
                return True
        else:
            data_nasc = self._data_nascimento
            
        idade = referencia.year - data_nasc.year - ((referencia.month, referencia.day) < (data_nasc.month, data_nasc.day))
        return idade >= 18

    def validar_independencia(self, data_atendimento=None):
        if not self.is_maior_de_idade(data_atendimento):
            data_str = data_atendimento if isinstance(data_atendimento, str) else datetime.now().strftime("%d/%m/%Y")
            raise PacienteMenorDeIdadeException(
                f"O paciente é MENOR DE IDADE na data agendada ({data_str}).\n"
                f"De acordo com as regras da clínica, não pode ser atendido de forma independente."
            )