class Profissional:
    def __init__(self, nome: str, celular: str, cpf: str, especialidade: str, registro_profissional: str, clinica):
        self._nome = nome
        self._celular = celular
        self._cpf = cpf
        self._especialidade = especialidade
        self._registro_profissional = registro_profissional
        self._clinica = clinica

    @property
    def nome(self):
        return self._nome

    @property
    def celular(self):
        return self._celular

    @property
    def cpf(self):
        return self._cpf

    @property
    def especialidade(self):
        return self._especialidade

    @property
    def registro_profissional(self):
        return self._registro_profissional

    @property
    def clinica(self):
        return self._clinica