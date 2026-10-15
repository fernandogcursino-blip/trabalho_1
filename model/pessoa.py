from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self._nome = nome
        self._celular = celular
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
        
    @property
    def celular(self):
        return self._celular
    
    @property
    def cpf(self):
        return self._cpf
        
    def __str__(self):
        return f"{self.__class__.__name__}(nome={self._nome}, cpf={self._cpf}, celular={self._celular})"