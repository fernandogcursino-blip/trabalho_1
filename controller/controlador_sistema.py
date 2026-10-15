from view.tela_sistema import TelaSistema
from controller.controlador_clinica import ControladorClinica
from controller.controlador_profissional import ControladorProfissional
from controller.controlador_paciente import ControladorPaciente
from controller.controlador_tipo_atendimento import ControladorTipoAtendimento
from controller.controlador_atendimento import ControladorAtendimento
from controller.controlador_relatorios import ControladorRelatorios

class ControladorSistema:
    def __init__(self):
        self._tela_sistema = TelaSistema(self)
        self._controlador_clinica = ControladorClinica(self)
        self._controlador_profissional = ControladorProfissional(self)
        self._controlador_paciente = ControladorPaciente(self)
        self._controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self._controlador_atendimento = ControladorAtendimento(self)
        self._controlador_relatorios = ControladorRelatorios(self)

    def inicializa_sistema(self):
        self.abre_tela_inicial()

    def cadastra_clinicas(self):
        self._controlador_clinica.inicia()

    def cadastra_profissionais(self):
        self._controlador_profissional.inicia()

    def cadastra_pacientes(self):
        self._controlador_paciente.inicia()

    def gerencia_tipos_atendimento(self):
        self._controlador_tipo_atendimento.inicia()

    def gerencia_atendimentos(self):
        self._controlador_atendimento.inicia()

    def emite_relatorios(self):
        self._controlador_relatorios.inicia()

    def encerra_sistema(self):
        exit(0)

    def abre_tela_inicial(self):
        switcher = {
            0: self.encerra_sistema,
            1: self.cadastra_clinicas,
            2: self.cadastra_profissionais,
            3: self.cadastra_pacientes,
            4: self.gerencia_tipos_atendimento,
            5: self.gerencia_atendimentos,
            6: self.emite_relatorios
        }

        while True:
            opcao = self._tela_sistema.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_sistema.mostra_mensagem("Opção inválida!"))
            funcao_escolhida()