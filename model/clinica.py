from datetime import time

class Clinica:
    def __init__(self, nome: str, localizacao: str, descricao: str, horario_abertura: time, horario_fechamento: time):
        self._nome = nome
        self._localizacao = localizacao
        self._descricao = descricao
        self._horario_abertura = horario_abertura
        self._horario_fechamento = horario_fechamento
        
    def verifica_horario_funcionamento(self, horario: time) -> bool:
        return self._horario_abertura <= horario <= self._horario_fechamento