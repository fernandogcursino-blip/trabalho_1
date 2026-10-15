from model import Paciente
from view.tela_paciente import TelaPaciente

class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self._tela_paciente = TelaPaciente(self)
        self._controlador_sistema = controlador_sistema
        self._pacientes = []

    @property
    def pacientes(self):
        return self._pacientes

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_paciente(self):
        dados = self._tela_paciente.pega_dados_paciente()
        if not dados:
            return
            
        if self.__paciente_existe(dados['cpf']):
            self._tela_paciente.mostra_mensagem("Erro: Paciente já cadastrado com este CPF.")
            return
            
        novo_paciente = Paciente(
            dados['nome'], 
            dados['cpf'], 
            dados['data_nascimento'], 
            dados['telefone']
        )
        self._pacientes.append(novo_paciente)
        self._tela_paciente.mostra_mensagem("Paciente cadastrado com sucesso!")
        
    def altera_paciente(self):
        cpf_antigo = self._tela_paciente.pega_cpf("CPF do paciente a alterar: ")
        if not cpf_antigo:
            return
            
        if not self.__paciente_existe(cpf_antigo):
            self._tela_paciente.mostra_mensagem("Paciente não encontrado.")
            return
            
        novos_dados = self._tela_paciente.pega_dados_paciente()
        if not novos_dados:
            return
            
        for i, paciente in enumerate(self._pacientes):
            if paciente.cpf == cpf_antigo:
                paciente_atualizado = Paciente(
                    novos_dados['nome'], 
                    novos_dados['cpf'], 
                    novos_dados['data_nascimento'], 
                    novos_dados['telefone']
                )
                self._pacientes[i] = paciente_atualizado
                self._tela_paciente.mostra_mensagem("Dados do paciente alterados com sucesso!")
                break
        
    def exclui_paciente(self):
        cpf = self._tela_paciente.pega_cpf("CPF do paciente a excluir: ")
        if not cpf:
            return
            
        for i, paciente in enumerate(self._pacientes):
            if paciente.cpf == cpf:
                del self._pacientes[i]
                self._tela_paciente.mostra_mensagem(f"Paciente com CPF {cpf} excluído com sucesso!")
                return
        self._tela_paciente.mostra_mensagem("Paciente não encontrado.")

    def lista_pacientes(self):
        if not self._pacientes:
            self._tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        self._tela_paciente.mostra_pacientes(self._pacientes)

    def retornar(self):
        return
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.inclui_paciente,
            2: self.altera_paciente,
            3: self.exclui_paciente,
            4: self.lista_pacientes
        }
        while True:
            opcao = self._tela_paciente.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_paciente.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break

    def __paciente_existe(self, cpf):
        for paciente in self._pacientes:
            if paciente.cpf == cpf:
                return True
        return False