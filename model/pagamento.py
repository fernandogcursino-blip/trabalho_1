from abc import ABC
from datetime import date

class Pagamento(ABC):
    def __init__(self, data_pagamento: date, atendimento, paciente, valor_pago: float):
        self._data_pagamento = data_pagamento
        self._atendimento = atendimento 
        self._paciente = paciente       
        self._valor_pago = valor_pago

    @property
    def valor_pago(self):
        return self._valor_pago

class PagamentoDinheiro(Pagamento):
    def __init__(self, data_pagamento: date, atendimento, paciente, valor_pago: float):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)

class PagamentoPix(Pagamento):
    def __init__(self, data_pagamento: date, atendimento, paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)
        self._cpf_pagador = cpf_pagador

class PagamentoCartao(Pagamento):
    def __init__(self, data_pagamento: date, atendimento, paciente, valor_pago: float, numero_cartao: str, bandeira: str):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)
        self._numero_cartao = numero_cartao
        self._bandeira = bandeira