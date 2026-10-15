from model.profissional import Profissional

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional: Profissional):
        self._descricao = descricao
        self._custo = custo
        self._profissional = profissional
        
    @property
    def descricao(self):
        return self._descricao

    @property
    def custo(self):
        return self._custo
        
    @property
    def profissional(self):
        return self._profissional

    def __str__(self):
        return f"Procedimento(descricao={self._descricao}, custo={self._custo}, profissional={self._profissional.nome})"