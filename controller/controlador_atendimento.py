from model import Atendimento
from view.tela_atendimento import TelaAtendimento

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self._tela_atendimento = TelaAtendimento(self)
        self._controlador_sistema = controlador_sistema
        self._atendimentos = []

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_atendimento(self):
        # 1. Buscar as listas dos outros controladores através do sistema
        pacientes_disponiveis = self._controlador_sistema.controlador_paciente.pacientes
        profissionais_disponiveis = self._controlador_sistema.controlador_profissional.profissionais
        clinicas_disponiveis = self._controlador_sistema.controlador_clinica.clinicas
        
        if not pacientes_disponiveis or not profissionais_disponiveis or not clinicas_disponiveis:
            self._tela_atendimento.mostra_mensagem("Erro: É necessário ter pelo menos um paciente, profissional e clínica cadastrados.")
            return

        # 2. A tela pede os dados e seleciona os objetos (você pode passar as listas para a tela mostrar e o usuário escolher por índice ou CPF/Nome)
        dados = self._tela_atendimento.pega_dados_atendimento(pacientes_disponiveis, profissionais_disponiveis, clinicas_disponiveis)
        if not dados:
            return

        try:
            # 3. Tenta criar o atendimento (as validações de exceção do Model vão rodar aqui)
            novo_atendimento = Atendimento(
                clinica=dados['clinica'],
                paciente=dados['paciente'],
                profissional=dados['profissional'],
                data_atendimento=dados['data'],
                horario_inicio=dados['horario_inicio'],
                horario_fim=dados['horario_fim'],
                tipo_atendimento=dados['tipo'],
                valor_base=dados['valor_base']
            )
            self._atendimentos.append(novo_atendimento)
            self._tela_atendimento.mostra_mensagem("Atendimento agendado com sucesso!")
            
        except Exception as e:
            # Captura as exceções personalizadas (Regra 1 e Regra 2) e mostra na tela
            self._tela_atendimento.mostra_mensagem(f"Erro ao agendar: {str(e)}")

    def lista_atendimentos(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        self._tela_atendimento.mostra_atendimentos(self._atendimentos)

    def retornar(self):
        self._controlador_sistema.abre_tela_inicial()
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.inclui_atendimento,
            2: self.adiciona_procedimento_no_atendimento,
            3: self.registra_pagamento,
            4: self.lista_atendimentos
        }
        while True:
            opcao = self._tela_atendimento.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_atendimento.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break