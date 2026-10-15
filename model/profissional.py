from model.pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome: str, cpf: str, celular: str, especialidade: str, registro_profissional: str, clinica):
        super().__init__(nome, cpf, celular)
        
        self._especialidade = especialidade
        self._registro_profissional = registro_profissional
        self._clinica = clinica

    @property
    def nome(self): return self._nome

    @property
    def cpf(self): return self._cpf

    @property
    def celular(self): return self._telefone  # Retorna o telefone herdado

    @property
    def especialidade(self): return self._especialidade

    @property
    def registro_profissional(self): return self._registro_profissional

    @property
    def clinica(self): return self._clinica