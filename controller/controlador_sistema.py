from controller.controlador_paciente import ControladorPaciente
from controller.controlador_profissional import ControladorProfissional
from controller.controlador_clinica import ControladorClinica
from controller.controlador_atendimento import ControladorAtendimento
from view.tela_sistema import TelaSistema
# Adicione depois o ControladorRelatorios

class ControladorSistema:
    def __init__(self):
        self._tela_sistema = TelaSistema(self)
        self._controlador_paciente = ControladorPaciente(self)
        self._controlador_profissional = ControladorProfissional(self)
        self._controlador_clinica = ControladorClinica(self)
        self._controlador_atendimento = ControladorAtendimento(self)

    @property
    def controlador_paciente(self):
        return self._controlador_paciente

    @property
    def controlador_profissional(self):
        return self._controlador_profissional
        
    @property
    def controlador_clinica(self):
        return self._controlador_clinica

    def inicializa_sistema(self):
        self.abre_tela_inicial()

    def cadastra_pacientes(self):
        self._controlador_paciente.inicia()

    def cadastra_profissionais(self):
        self._controlador_profissional.inicia()

    def cadastra_clinicas(self):
        self._controlador_clinica.inicia()

    def gerencia_atendimentos(self):
        self._controlador_atendimento.inicia()

    def encerra_sistema(self):
        exit(0)

    def abre_tela_inicial(self):
        switcher = {
            0: self.encerra_sistema,
            1: self.cadastra_clinicas,
            2: self.cadastra_profissionais,
            3: self.cadastra_pacientes,
            4: self.gerencia_atendimentos
        }
        while True:
            opcao = self._tela_sistema.mostra_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_sistema.mostra_mensagem("Opção inválida"))
            funcao_escolhida()