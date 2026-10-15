from datetime import datetime

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
        
    def verifica_horario_funcionamento(self, horario) -> bool:
        """
        Recebe um objeto 'time' (horário do atendimento) e verifica se 
        está dentro do intervalo de funcionamento da clínica.
        """
        # Converte as strings guardadas (ex: "08:00") para objetos time antes de comparar
        abertura = datetime.strptime(self._horario_abertura, "%H:%M").time()
        fechamento = datetime.strptime(self._horario_fechamento, "%H:%M").time()
        
        return abertura <= horario <= fechamento