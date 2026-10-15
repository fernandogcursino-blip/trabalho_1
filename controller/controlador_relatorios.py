from view.tela_relatorios import TelaRelatorios

class ControladorRelatorios:
    def __init__(self, controlador_sistema):
        self._controlador_sistema = controlador_sistema
        self._tela_relatorios = TelaRelatorios(self)

    def inicia(self):
        self.abre_tela_inicial()

    def _obter_atendimentos(self):
        # Acede à lista de atendimentos através do controlador principal
        return self._controlador_sistema.controlador_atendimento._atendimentos

    def relatorio_clinicas_mais_atendimentos(self):
        atendimentos = self._obter_atendimentos()
        if not atendimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum atendimento registado para gerar o relatório.")
            return

        # Dicionário para contar { "Nome da Clínica": Quantidade }
        contagem = {}
        for atendimento in atendimentos:
            nome_clinica = atendimento._clinica._nome
            contagem[nome_clinica] = contagem.get(nome_clinica, 0) + 1
            
        # Ordena do maior para o menor
        clinicas_ordenadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        
        dados_formatados = [f"{clinica}: {qtd} atendimento(s)" for clinica, qtd in clinicas_ordenadas]
        self._tela_relatorios.mostra_dados_relatorio("Clínicas com Maior Número de Atendimentos", dados_formatados)

    def relatorio_atendimentos_caros_baratos(self):
        atendimentos = self._obter_atendimentos()
        if not atendimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum atendimento registado.")
            return

        # Ordena a lista usando o método calcular_valor_total() que criaste no Model
        atendimentos_ordenados = sorted(atendimentos, key=lambda a: a.calcular_valor_total())
        
        mais_barato = atendimentos_ordenados[0]
        mais_caro = atendimentos_ordenados[-1]

        dados = [
            f"Mais Barato: Paciente {mais_barato._paciente.nome} - Total: R$ {mais_barato.calcular_valor_total():.2f}",
            f"Mais Caro: Paciente {mais_caro._paciente.nome} - Total: R$ {mais_caro.calcular_valor_total():.2f}"
        ]
        self._tela_relatorios.mostra_dados_relatorio("Atendimentos Mais Caros e Mais Baratos", dados)

    def relatorio_procedimentos_populares(self):
        atendimentos = self._obter_atendimentos()
        if not atendimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum atendimento registado.")
            return

        contagem = {}
        for atendimento in atendimentos:
            for procedimento in atendimento._procedimentos:
                desc = procedimento.descricao
                contagem[desc] = contagem.get(desc, 0) + 1

        if not contagem:
            self._tela_relatorios.mostra_mensagem("Nenhum procedimento foi realizado nos atendimentos atuais.")
            return

        procedimentos_ordenados = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        dados = [f"{desc}: {qtd} vez(es)" for desc, qtd in procedimentos_ordenados]
        self._tela_relatorios.mostra_dados_relatorio("Procedimentos Mais Realizados (Populares)", dados)

    def relatorio_procedimentos_valores(self):
        atendimentos = self._obter_atendimentos()
        todos_procedimentos = []
        for atendimento in atendimentos:
            todos_procedimentos.extend(atendimento._procedimentos)

        if not todos_procedimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum procedimento registado.")
            return

        procedimentos_ordenados = sorted(todos_procedimentos, key=lambda p: p.custo)
        mais_barato = procedimentos_ordenados[0]
        mais_caro = procedimentos_ordenados[-1]

        dados = [
            f"Mais Barato: {mais_barato.descricao} - R$ {mais_barato.custo:.2f}",
            f"Mais Caro: {mais_caro.descricao} - R$ {mais_caro.custo:.2f}"
        ]
        self._tela_relatorios.mostra_dados_relatorio("Procedimentos Mais Caros e Mais Baratos", dados)

    def retornar(self):
        self._controlador_sistema.abre_tela_inicial()
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.relatorio_clinicas_mais_atendimentos,
            2: self.relatorio_atendimentos_caros_baratos,
            3: self.relatorio_procedimentos_populares,
            4: self.relatorio_procedimentos_valores
        }
        while True:
            opcao = self._tela_relatorios.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao)
            funcao_escolhida()
            if opcao == 0:
                break