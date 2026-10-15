from model import Clinica
from view.tela_clinica import TelaClinica

class ControladorClinica:
    def __init__(self, controlador_sistema):
        self._tela_clinica = TelaClinica(self)
        self._controlador_sistema = controlador_sistema
        self._clinicas = []

    @property
    def clinicas(self):
        return self._clinicas

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_clinica(self):
        dados = self._tela_clinica.pega_dados_clinica()
        if not dados:
            return
            
        nova_clinica = Clinica(
            dados['nome'], dados['localizacao'], dados['descricao'], 
            dados['horario_abertura'], dados['horario_fechamento']
        )
        self._clinicas.append(nova_clinica)
        self._tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")
        
    # Implemente altera_clinica e exclui_clinica
    
    def lista_clinicas(self):
        if not self._clinicas:
            self._tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        self._tela_clinica.mostra_clinicas(self._clinicas)

    def retornar(self):
        self._controlador_sistema.abre_tela_inicial()
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.inclui_clinica,
            2: self.altera_clinica,
            3: self.exclui_clinica,
            4: self.lista_clinicas
        }
        while True:
            opcao = self._tela_clinica.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_clinica.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break