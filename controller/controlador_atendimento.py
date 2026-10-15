from view.tela_atendimento import TelaAtendimento
from model import Atendimento, Procedimento

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self._tela_atendimento = TelaAtendimento(self)
        self._controlador_sistema = controlador_sistema
        self._atendimentos = []

    @property
    def atendimentos(self):
        return self._atendimentos

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_atendimento(self):
        pacientes = self._controlador_sistema._controlador_paciente.pacientes
        profissionais = self._controlador_sistema._controlador_profissional.profissionais
        
        if not pacientes or not profissionais:
            self._tela_atendimento.mostra_mensagem("Erro: É preciso ter pelo menos 1 Paciente e 1 Profissional cadastrados!")
            return

        dados = self._tela_atendimento.pega_dados_atendimento(pacientes, profissionais)
        if not dados:
            return
            
        # Cria o atendimento passando TODOS os 8 argumentos exigidos
        novo_atendimento = Atendimento(
            dados['codigo'], 
            dados['paciente'], 
            dados['profissional'], 
            dados['data'], 
            dados['horario'],
            dados['horario_fim'],
            dados['tipo_atendimento'],
            dados['valor_base']
        )
        self._atendimentos.append(novo_atendimento)
        self._tela_atendimento.mostra_mensagem("Atendimento criado com sucesso!")

    def adiciona_procedimento_no_atendimento(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado para adicionar procedimentos.")
            return

        codigo = self._tela_atendimento.le_num_inteiro("Código do Atendimento: ")
        
        atendimento_encontrado = None
        for atendimento in self._atendimentos:
            codigo_atual = atendimento.codigo if hasattr(atendimento, 'codigo') else atendimento._codigo
            if codigo_atual == codigo:
                atendimento_encontrado = atendimento
                break
                
        if not atendimento_encontrado:
            self._tela_atendimento.mostra_mensagem("Atendimento não encontrado.")
            return
            
        dados_procedimento = self._tela_atendimento.pega_dados_procedimento()
        if dados_procedimento:
            novo_procedimento = Procedimento(
                dados_procedimento['nome'], 
                dados_procedimento['valor']
            )
            if hasattr(atendimento_encontrado, 'adiciona_procedimento'):
                atendimento_encontrado.adiciona_procedimento(novo_procedimento)
            else:
                atendimento_encontrado._procedimentos.append(novo_procedimento)
            self._tela_atendimento.mostra_mensagem("Procedimento adicionado com sucesso!")

    def lista_atendimentos(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        self._tela_atendimento.mostra_atendimentos(self._atendimentos)

    def retornar(self):
        # Apenas encerra o método, cortando o loop infinito
        return
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.inclui_atendimento,
            2: self.adiciona_procedimento_no_atendimento,
            3: self.lista_atendimentos
        }
        while True:
            opcao = self._tela_atendimento.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_atendimento.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break