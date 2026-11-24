from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, telefone: str):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def telefone(self) -> str:
        return self._telefone
        
    def __str__(self):
        return f"{self.__class__.__name__}(nome={self._nome}, cpf={self._cpf}, celular={self._celular})"