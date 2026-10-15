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
            
        if self.__clinica_existe(dados['cnpj']):
            self._tela_clinica.mostra_mensagem("Erro: Clínica já cadastrada com este CNPJ.")
            return
            
        nova_clinica = Clinica(
            dados['nome'], dados['cnpj'], dados['endereco'],
            dados['horario_abertura'], dados['horario_fechamento']
        )
        self._clinicas.append(nova_clinica)
        self._tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")
        
    def altera_clinica(self):
        cnpj_antigo = self._tela_clinica.pega_cnpj("CNPJ da clínica a alterar: ")
        if not cnpj_antigo:
            return
            
        if not self.__clinica_existe(cnpj_antigo):
            self._tela_clinica.mostra_mensagem("Clínica não encontrada.")
            return
            
        novos_dados = self._tela_clinica.pega_dados_clinica()
        if not novos_dados:
            return
            
        for i, clinica in enumerate(self._clinicas):
            cnpj_atual = clinica.cnpj if hasattr(clinica, 'cnpj') else clinica._cnpj
            if cnpj_atual == cnpj_antigo:
                clinica_atualizada = Clinica(
                    novos_dados['nome'], novos_dados['cnpj'], novos_dados['endereco'],
                    novos_dados['horario_abertura'], novos_dados['horario_fechamento']
                )
                self._clinicas[i] = clinica_atualizada
                self._tela_clinica.mostra_mensagem("Dados da clínica alterados com sucesso!")
                break
        
    def exclui_clinica(self):
        cnpj = self._tela_clinica.pega_cnpj("CNPJ da clínica a excluir: ")
        if not cnpj:
            return
            
        for i, clinica in enumerate(self._clinicas):
            cnpj_atual = clinica.cnpj if hasattr(clinica, 'cnpj') else clinica._cnpj
            if cnpj_atual == cnpj:
                del self._clinicas[i]
                self._tela_clinica.mostra_mensagem(f"Clínica com CNPJ {cnpj} excluída com sucesso!")
                return
        self._tela_clinica.mostra_mensagem("Clínica não encontrada.")

    def lista_clinicas(self):
        if not self._clinicas:
            self._tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        self._tela_clinica.mostra_clinicas(self._clinicas)

    # CORREÇÃO CRÍTICA DO LOOP AQUI:
    def retornar(self):
        return
    
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

    def __clinica_existe(self, cnpj):
        for clinica in self._clinicas:
            cnpj_atual = clinica.cnpj if hasattr(clinica, 'cnpj') else clinica._cnpj
            if cnpj_atual == cnpj:
                return True
        return False