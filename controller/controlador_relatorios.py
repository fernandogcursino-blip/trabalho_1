from view.tela_relatorios import TelaRelatorios

class ControladorRelatorios:
    def __init__(self, controlador_sistema):
        self._tela_relatorios = TelaRelatorios(self)
        self._controlador_sistema = controlador_sistema

    def inicia(self):
        self.abre_tela_inicial()

    def relatorio_clinicas_mais_atendimentos(self):
        atendimentos = self._controlador_sistema._controlador_atendimento.atendimentos
        
        if not atendimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum atendimento cadastrado para gerar o relatório.")
            return
        
        contagem_clinicas = {}
        for atendimento in atendimentos:
            clinica = atendimento.profissional.clinica
            nome_clinica = clinica.nome
            
            if nome_clinica in contagem_clinicas:
                contagem_clinicas[nome_clinica] += 1
            else:
                contagem_clinicas[nome_clinica] = 1
                
        clinicas_ordenadas = sorted(contagem_clinicas.items(), key=lambda item: item[1], reverse=True)
        self._tela_relatorios.mostra_relatorio_clinicas(clinicas_ordenadas)

    def relatorio_atendimentos_caros_baratos(self):
        atendimentos = self._controlador_sistema._controlador_atendimento.atendimentos
        if not atendimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum atendimento cadastrado para gerar o relatório.")
            return
        
        lista_valores = []
        for a in atendimentos:
            valor_total = a.valor_base
            for p in a.procedimentos:
                valor_total += p.valor
            lista_valores.append((a, valor_total))
        
        atendimentos_ordenados = sorted(lista_valores, key=lambda item: item[1], reverse=True)
        self._tela_relatorios.mostra_relatorio_atendimentos_valores(atendimentos_ordenados)

    def relatorio_procedimentos_mais_realizados(self):
        atendimentos = self._controlador_sistema._controlador_atendimento.atendimentos
        contagem_procedimentos = {}
        
        for a in atendimentos:
            for p in a.procedimentos:
                nome_proc = p.nome
                if nome_proc in contagem_procedimentos:
                    contagem_procedimentos[nome_proc] += 1
                else:
                    contagem_procedimentos[nome_proc] = 1
        
        if not contagem_procedimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum procedimento cadastrado nos atendimentos.")
            return
            
        procedimentos_ordenados = sorted(contagem_procedimentos.items(), key=lambda item: item[1], reverse=True)
        self._tela_relatorios.mostra_relatorio_procedimentos_realizados(procedimentos_ordenados)

    def relatorio_procedimentos_caros_baratos(self):
        atendimentos = self._controlador_sistema._controlador_atendimento.atendimentos
        valores_procedimentos = {}
        
        for a in atendimentos:
            for p in a.procedimentos:
                nome_proc = p.nome
                if nome_proc not in valores_procedimentos:
                    valores_procedimentos[nome_proc] = p.valor
        
        if not valores_procedimentos:
            self._tela_relatorios.mostra_mensagem("Nenhum procedimento cadastrado nos atendimentos.")
            return
            
        procedimentos_ordenados = sorted(valores_procedimentos.items(), key=lambda item: item[1], reverse=True)
        self._tela_relatorios.mostra_relatorio_procedimentos_valores(procedimentos_ordenados)

    def retornar(self):
        return
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar,
            1: self.relatorio_clinicas_mais_atendimentos,
            2: self.relatorio_atendimentos_caros_baratos,
            3: self.relatorio_procedimentos_mais_realizados,
            4: self.relatorio_procedimentos_caros_baratos
        }
        while True:
            opcao = self._tela_relatorios.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_relatorios.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break