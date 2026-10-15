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
        dados = self._tela_profissional.pega_dados_profissional()
        if not dados:
            return
            
        if self.__profissional_existe(dados['cpf']):
            self._tela_profissional.mostra_mensagem("Erro: Profissional já cadastrado.")
            return
            
        novo_profissional = Profissional(
            dados['nome'], dados['celular'], dados['cpf'], 
            dados['especialidade'], dados['registro_profissional']
        )
        self._profissionais.append(novo_profissional)
        self._tela_profissional.mostra_mensagem("Profissional cadastrado com sucesso!")
        
    # Implemente altera_profissional e exclui_profissional seguindo a lógica do Paciente
    
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
            # 2: self.altera_profissional,
            # 3: self.exclui_profissional,
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