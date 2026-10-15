from model.pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, especialidade: str, registro_profissional: str):
        super().__init__(nome, celular, cpf)
        self._especialidade = especialidade
        self._registro_profissional = registro_profissional