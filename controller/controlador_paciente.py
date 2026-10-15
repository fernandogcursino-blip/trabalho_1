from model.paciente import Paciente
from view.tela_paciente import TelaPaciente

class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self._tela_paciente = TelaPaciente(self)
        self._controlador_sistema = controlador_sistema
        self._pacientes = []

    def inicia(self):
        """Inicia o menu de pacientes."""
        self.abre_tela_inicial()

    def inclui_paciente(self):
        dados_paciente = self._tela_paciente.pega_dados_paciente()
        if not dados_paciente:
            return
            
        cpf = dados_paciente['cpf']
        if self.__paciente_existe(cpf):
            self._tela_paciente.mostra_mensagem(f"Erro: Paciente com CPF {cpf} já existe.")
            return
            
        novo_paciente = Paciente(
            dados_paciente['nome'], 
            dados_paciente['celular'], 
            cpf, 
            dados_paciente['data_nascimento']
        )
        self._pacientes.append(novo_paciente)
        self._tela_paciente.mostra_mensagem(f"Paciente {dados_paciente['nome']} cadastrado com sucesso!")
        
    def altera_paciente(self):
        """Altera os dados de um paciente existente."""
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
                self._pacientes[i]._nome = novos_dados['nome']
                self._pacientes[i]._celular = novos_dados['celular']
                self._pacientes[i]._cpf = novos_dados['cpf']
                self._pacientes[i]._data_nascimento = novos_dados['data_nascimento']
                self._tela_paciente.mostra_mensagem("Dados do paciente alterados com sucesso!")
                break
        
    def exclui_paciente(self):
        """Exclui um paciente pelo CPF."""
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
        """Lista todos os pacientes."""
        if not self._pacientes:
            self._tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        self._tela_paciente.mostra_pacientes(self._pacientes)

    def retornar(self):
        """Retorna ao menu principal."""
        self._controlador_sistema.abre_tela_inicial()
    
    def abre_tela_inicial(self):
        """Abre o menu principal de pacientes."""
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
        """Verifica se um paciente com este CPF já existe."""
        return any(paciente.cpf == cpf for paciente in self._pacientes)