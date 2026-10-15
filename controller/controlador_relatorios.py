from view.tela_relatorios import TelaRelatorios

class ControladorRelatorios:
    def __init__(self, controlador_sistema):
        self._tela_relatorios = TelaRelatorios(self)
        self._controlador_sistema = controlador_sistema

    def inicia(self):
        self.abre_tela_inicial()

    def relatorio_clinicas_mais_atendimentos(self):
        # Acede aos atendimentos instanciados no controlador de atendimentos
        atendimentos = self._controlador_sistema._controlador_atendimento.atendimentos
        
        if not atendimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum atendimento cadastrado para gerar o relatório.")
            return
        
        contagem_clinicas = {}
        
        for atendimento in atendimentos:
            # O CAMINHO CORRETO: O atendimento tem um profissional, que por sua vez tem uma clínica
            clinica = atendimento.profissional.clinica
            nome_clinica = clinica.nome
            
            if nome_clinica in contagem_clinicas:
                contagem_clinicas[nome_clinica] += 1
            else:
                contagem_clinicas[nome_clinica] = 1
                
        # Ordena o dicionário de forma decrescente com base no número de atendimentos
        clinicas_ordenadas = sorted(contagem_clinicas.items(), key=lambda item: item[1], reverse=True)
        
        self._tela_relatorios.mostra_relatorio_clinicas(clinicas_ordenadas)

    def retornar(self):
        # Apenas encerra o método, fechando o loop limpamente
        return
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.relatorio_clinicas_mais_atendimentos
            # Pode adicionar opções 2, 3, etc., se tiver outros relatórios
        }
        while True:
            opcao = self._tela_relatorios.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_relatorios.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break