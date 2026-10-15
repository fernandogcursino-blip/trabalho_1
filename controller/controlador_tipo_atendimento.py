from view.tela_tipo_atendimento import TelaTipoAtendimento
from model.tipo_atendimento import TipoAtendimento

class ControladorTipoAtendimento:
    def __init__(self, controlador_sistema):
        self._tela_tipo = TelaTipoAtendimento(self)
        self._controlador_sistema = controlador_sistema
        self._tipos = []

    @property
    def tipos(self):
        return self._tipos

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_tipo(self):
        dados = self._tela_tipo.pega_dados_tipo()
        if not dados: return
        
        if self.__tipo_existe(dados['codigo']):
            self._tela_tipo.mostra_mensagem("Erro: Tipo já cadastrado com este código.")
            return
            
        novo_tipo = TipoAtendimento(dados['codigo'], dados['nome'], dados['descricao'])
        self._tipos.append(novo_tipo)
        self._tela_tipo.mostra_mensagem("Tipo de atendimento cadastrado com sucesso!")

    def altera_tipo(self):
        if not self._tipos:
            self._tela_tipo.mostra_mensagem("Nenhum tipo cadastrado.")
            return
            
        codigo = self._tela_tipo.le_num_inteiro("Código do tipo a alterar: ")
        
        for i, tipo in enumerate(self._tipos):
            if tipo.codigo == codigo:
                novos_dados = self._tela_tipo.pega_dados_tipo()
                self._tipos[i] = TipoAtendimento(novos_dados['codigo'], novos_dados['nome'], novos_dados['descricao'])
                self._tela_tipo.mostra_mensagem("Tipo alterado com sucesso!")
                return
        self._tela_tipo.mostra_mensagem("Tipo não encontrado.")

    def exclui_tipo(self):
        if not self._tipos:
            self._tela_tipo.mostra_mensagem("Nenhum tipo cadastrado.")
            return
            
        codigo = self._tela_tipo.le_num_inteiro("Código do tipo a excluir: ")
        for i, tipo in enumerate(self._tipos):
            if tipo.codigo == codigo:
                del self._tipos[i]
                self._tela_tipo.mostra_mensagem(f"Tipo {codigo} excluído com sucesso!")
                return
        self._tela_tipo.mostra_mensagem("Tipo não encontrado.")

    def lista_tipos(self):
        if not self._tipos:
            self._tela_tipo.mostra_mensagem("Nenhum tipo cadastrado.")
            return
        self._tela_tipo.mostra_tipos(self._tipos)

    def retornar(self):
        return

    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar, 1: self.inclui_tipo, 2: self.altera_tipo,
            3: self.exclui_tipo, 4: self.lista_tipos
        }
        while True:
            opcao = self._tela_tipo.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_tipo.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break

    def __tipo_existe(self, codigo):
        return any(t.codigo == codigo for t in self._tipos)