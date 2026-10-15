class Procedimento:
    def __init__(self, nome: str, valor: float, profissional):
        self._nome = nome
        self._valor = valor
        self._profissional = profissional

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor
        
    @property
    def profissional(self):
        return self._profissional