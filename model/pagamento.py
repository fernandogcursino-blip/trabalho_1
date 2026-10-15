from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, data: str, atendimento, paciente, valor_pago: float):
        self._data = data
        self._atendimento = atendimento
        self._paciente = paciente
        self._valor_pago = valor_pago

    @property
    def data(self): return self._data
    
    @property
    def atendimento(self): return self._atendimento
    
    @property
    def paciente(self): return self._paciente
    
    @property
    def valor_pago(self): return self._valor_pago

    @abstractmethod
    def detalhe(self):
        pass

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: str, atendimento, paciente, valor_pago: float):
        super().__init__(data, atendimento, paciente, valor_pago)

    def detalhe(self):
        return "Dinheiro"

class PagamentoPix(Pagamento):
    def __init__(self, data: str, atendimento, paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self._cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self): return self._cpf_pagador

    def detalhe(self):
        return f"PIX (CPF: {self._cpf_pagador})"

class PagamentoCartao(Pagamento):
    def __init__(self, data: str, atendimento, paciente, valor_pago: float, numero_cartao: str, bandeira: str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self._numero_cartao = numero_cartao
        self._bandeira = bandeira

    @property
    def numero_cartao(self): return self._numero_cartao
    
    @property
    def bandeira(self): return self._bandeira

    def detalhe(self):
        # Exibe a bandeira e apenas os últimos 4 dígitos do cartão
        final_cartao = self._numero_cartao[-4:] if len(self._numero_cartao) >= 4 else self._numero_cartao
        return f"Cartão {self._bandeira} (Final {final_cartao})"