from datetime import datetime

class Atendimento:
    def __init__(self, codigo, paciente, profissional, data, horario_inicio, horario_fim, tipo_atendimento, valor_base):
        self._codigo = codigo
        self._paciente = paciente
        self._profissional = profissional
        self._data = data
        self._horario_inicio = horario_inicio
        self._horario_fim = horario_fim
        self._tipo_atendimento = tipo_atendimento
        self._valor_base = float(valor_base)
        self._procedimentos = []
        self._pagamentos = [] 

        self._paciente.validar_independencia(self._data)

        clinica = self._profissional.clinica
        try:
            inicio_time = datetime.strptime(horario_inicio, "%H:%M").time()
            fim_time = datetime.strptime(horario_fim, "%H:%M").time()
            
            if hasattr(clinica, 'verifica_horario_funcionamento'):
                if not clinica.verifica_horario_funcionamento(inicio_time):
                    raise ValueError(f"O horário de início ({horario_inicio}) está fora do expediente da clínica '{clinica.nome}' (Aberto das {clinica.horario_abertura} às {clinica.horario_fechamento}).")
                if not clinica.verifica_horario_funcionamento(fim_time):
                    raise ValueError(f"O horário de fim ({horario_fim}) ultrapassa o expediente da clínica '{clinica.nome}' (Aberto das {clinica.horario_abertura} às {clinica.horario_fechamento}).")
        except ValueError as e:
            raise ValueError(str(e))

    @property
    def codigo(self): return self._codigo
    @property
    def paciente(self): return self._paciente
    @property
    def profissional(self): return self._profissional
    @property
    def data(self): return self._data
    @property
    def horario_inicio(self): return self._horario_inicio
    @property
    def horario_fim(self): return self._horario_fim
    @property
    def tipo_atendimento(self): return self._tipo_atendimento
    @property
    def valor_base(self): return self._valor_base
    @property
    def procedimentos(self): return self._procedimentos
    @property
    def pagamentos(self): return self._pagamentos

    def adiciona_procedimento(self, procedimento):
        self._procedimentos.append(procedimento)

    def adiciona_pagamento(self, pagamento):
        self._pagamentos.append(pagamento)

    def calcula_valor_total(self):
        total = float(self._valor_base)
        for p in self._procedimentos:
            valor_p = p.valor if hasattr(p, 'valor') else getattr(p, '_valor', 0.0)
            total += float(valor_p)
        return total

    def calcula_valor_restante(self):
        total = self.calcula_valor_total()
        pago = 0.0
        for pag in self._pagamentos:
            valor_pag = pag.valor_pago if hasattr(pag, 'valor_pago') else getattr(pag, '_valor_pago', 0.0)
            pago += float(valor_pag)
        return total - pago

    @property
    def status_pagamento(self):
        restante = self.calcula_valor_restante()
        if restante <= 0:
            return "Pago"
        elif restante < self.calcula_valor_total():
            return "Parcialmente Pago"
        else:
            return "Pendente"