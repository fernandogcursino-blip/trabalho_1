from datetime import time

class Clinica:
    def __init__(self, nome: str, cnpj: str, endereco: str, horario_abertura: str, horario_fechamento: str):
        self._nome = nome
        self._cnpj = cnpj
        self._endereco = endereco
        self._horario_abertura = horario_abertura
        self._horario_fechamento = horario_fechamento

    @property
    def nome(self):
        return self._nome

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def endereco(self):
        return self._endereco

    @property
    def horario_abertura(self):
        return self._horario_abertura

    @property
    def horario_fechamento(self):
        return self._horario_fechamento
        
    def verifica_horario_funcionamento(self, horario: time) -> bool:
        abertura = datetime.strptime(self._horario_abertura, "%H:%M").time()
        fechamento = datetime.strptime(self._horario_fechamento, "%H:%M").time()
        
        return abertura <= horario <= fechamento