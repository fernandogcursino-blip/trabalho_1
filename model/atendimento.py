from datetime import date, time
from model.clinica import Clinica
from model.paciente import Paciente
from model.profissional import Profissional
from model.procedimento import Procedimento
from model.pagamento import Pagamento
from model.excecoes import HorarioInvalidoException, DataPagamentoInvalidaException

class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional, 
                 data_atendimento: date, horario_inicio: time, horario_fim: time, tipo_atendimento: str, valor_base: float):
        
        # Validação Regra 1
        paciente.validar_independencia()
        
        # Validação Regra 2
        if not clinica.verifica_horario_funcionamento(horario_inicio) or not clinica.verifica_horario_funcionamento(horario_fim):
            raise HorarioInvalidoException("O atendimento está fora do horário de funcionamento da clínica.")

        self._clinica = clinica              
        self._paciente = paciente            
        self._profissional = profissional    
        self._data_atendimento = data_atendimento
        self._horario_inicio = horario_inicio
        self._horario_fim = horario_fim
        self._tipo_atendimento = tipo_atendimento
        self._valor_base = valor_base
        
        self._procedimentos = [] 
        self._pagamentos = []    

    def adicionar_procedimento(self, procedimento: Procedimento):
        self._procedimentos.append(procedimento)

    def adicionar_pagamento(self, pagamento: Pagamento):
        # Validação Regra 3
        if pagamento._data_pagamento > self._data_atendimento:
            raise DataPagamentoInvalidaException("O pagamento deve ser realizado até a data do atendimento.")
        self._pagamentos.append(pagamento)

    def calcular_valor_total(self) -> float:
        total_procedimentos = sum(p.custo for p in self._procedimentos)
        return self._valor_base + total_procedimentos

    def calcular_valor_restante(self) -> float:
        total_pago = sum(p.valor_pago for p in self._pagamentos)
        return self.calcular_valor_total() - total_pago