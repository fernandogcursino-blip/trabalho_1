from model import Profissional
from view.tela_profissional import TelaProfissional

class ControladorProfissional:
    def __init__(self, controlador_sistema):
        self._tela_profissional = TelaProfissional(self)
        self._controlador_sistema = controlador_sistema
        self._profissionais = []

    @property
    def profissionais(self):
        return self._profissionais

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_profissional(self):
        # Acessa a lista de clínicas instanciada no sistema central
        clinicas = self._controlador_sistema._controlador_clinica.clinicas
        
        if not clinicas:
            self._tela_profissional.mostra_mensagem("Erro: É obrigatório cadastrar uma Clínica primeiro!")
            return

        dados = self._tela_profissional.pega_dados_profissional(clinicas)
        if not dados:
            return
            
        if self.__profissional_existe(dados['cpf']):
            self._tela_profissional.mostra_mensagem("Erro: Profissional já cadastrado.")
            return
            
        novo_profissional = Profissional(
            dados['nome'], dados['celular'], dados['cpf'], 
            dados['especialidade'], dados['registro_profissional'],
            dados['clinica']
        )
        self._profissionais.append(novo_profissional)
        self._tela_profissional.mostra_mensagem("Profissional cadastrado e vinculado à clínica com sucesso!")
        
    def altera_profissional(self):
        cpf_antigo = self._tela_profissional.pega_cpf("CPF do profissional a alterar: ")
        if not cpf_antigo:
            return
            
        if not self.__profissional_existe(cpf_antigo):
            self._tela_profissional.mostra_mensagem("Profissional não encontrado.")
            return
            
        clinicas = self._controlador_sistema._controlador_clinica.clinicas
        novos_dados = self._tela_profissional.pega_dados_profissional(clinicas)
        if not novos_dados:
            return
            
        for i, profissional in enumerate(self._profissionais):
            if profissional.cpf == cpf_antigo:
                profissional_atualizado = Profissional(
                    novos_dados['nome'], novos_dados['celular'], novos_dados['cpf'], 
                    novos_dados['especialidade'], novos_dados['registro_profissional'],
                    novos_dados['clinica']
                )
                self._profissionais[i] = profissional_atualizado
                self._tela_profissional.mostra_mensagem("Dados do profissional alterados com sucesso!")
                break
        
    def exclui_profissional(self):
        cpf = self._tela_profissional.pega_cpf("CPF do profissional a excluir: ")
        if not cpf:
            return
            
        for i, profissional in enumerate(self._profissionais):
            if profissional.cpf == cpf:
                del self._profissionais[i]
                self._tela_profissional.mostra_mensagem(f"Profissional com CPF {cpf} excluído com sucesso!")
                return
        self._tela_profissional.mostra_mensagem("Profissional não encontrado.")

    def lista_profissionais(self):
        if not self._profissionais:
            self._tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        self._tela_profissional.mostra_profissionais(self._profissionais)

    def retornar(self):
        self._controlador_sistema.abre_tela_inicial()
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.inclui_profissional,
            2: self.altera_profissional,
            3: self.exclui_profissional,
            4: self.lista_profissionais
        }
        while True:
            opcao = self._tela_profissional.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_profissional.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break

    def __profissional_existe(self, cpf):
        return any(p.cpf == cpf for p in self._profissionais)