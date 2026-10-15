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
        self._valor_base = valor_base
        self._procedimentos = []

        # 1. Valida o paciente
        self._paciente.validar_independencia()

        # 2. Puxa a clínica do profissional de forma segura
        clinica = self._profissional.clinica
        
        # 3. Converte os horários digitados (strings) para objetos 'time' para poder comparar
        try:
            inicio_time = datetime.strptime(horario_inicio, "%H:%M").time()
            fim_time = datetime.strptime(horario_fim, "%H:%M").time()
            
            # Verifica se a clínica armazenada é um objeto válido e compara os horários
            if hasattr(clinica, 'verifica_horario_funcionamento'):
                if not clinica.verifica_horario_funcionamento(inicio_time) or not clinica.verifica_horario_funcionamento(fim_time):
                    raise ValueError("O horário escolhido ultrapassa o horário de funcionamento da clínica!")
        except ValueError as e:
            raise ValueError(f"Erro no agendamento: {e}")

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

    def adiciona_procedimento(self, procedimento):
        self._procedimentos.append(procedimento)