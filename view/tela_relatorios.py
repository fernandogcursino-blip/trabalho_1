class TelaRelatorios:
    def __init__(self, controlador):
        self._controlador = controlador

    def le_num_inteiro(self, mensagem: str = "", inteiros_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um número inteiro válido.")
                if inteiros_validos:
                    print(f"Valores válidos: {inteiros_validos}")

    def mostra_tela_opcoes(self):
        print("\n--- MENU DE RELATÓRIOS ---")
        print("1 - Relatório de Clínicas com mais atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados (populares)")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def mostra_relatorio_clinicas(self, clinicas_ordenadas):
        print("\n--- RELATÓRIO: CLÍNICAS COM MAIS ATENDIMENTOS ---")
        for posicao, (nome_clinica, quantidade) in enumerate(clinicas_ordenadas, start=1):
            texto_atendimento = "atendimento" if quantidade == 1 else "atendimentos"
            print(f"{posicao}º Lugar: {nome_clinica} - {quantidade} {texto_atendimento}")
        print("-" * 50)

    def mostra_relatorio_atendimentos_valores(self, atendimentos_ordenados):
        print("\n--- RELATÓRIO: ATENDIMENTOS MAIS CAROS E MAIS BARATOS ---")
        if not atendimentos_ordenados:
            print("Nenhum dado para exibir.")
            return
            
        mais_caro, valor_caro = atendimentos_ordenados[0]
        print(f"[MAIS CARO] -> Código: {mais_caro.codigo} | Valor Total: R$ {valor_caro:.2f} | Paciente: {mais_caro.paciente.nome}")
        
        mais_barato, valor_barato = atendimentos_ordenados[-1]
        print(f"[MAIS BARATO] -> Código: {mais_barato.codigo} | Valor Total: R$ {valor_barato:.2f} | Paciente: {mais_barato.paciente.nome}")
        
        print("\nRanking Completo:")
        for posicao, (a, valor) in enumerate(atendimentos_ordenados, start=1):
            print(f"{posicao}º - Atendimento {a.codigo} (Paciente: {a.paciente.nome}) - R$ {valor:.2f}")
        print("-" * 50)

    def mostra_relatorio_procedimentos_realizados(self, procedimentos_ordenados):
        print("\n--- RELATÓRIO: PROCEDIMENTOS MAIS REALIZADOS ---")
        if not procedimentos_ordenados:
            print("Nenhum procedimento registrado nos atendimentos.")
            return
            
        for posicao, (nome_proc, quantidade) in enumerate(procedimentos_ordenados, start=1):
            texto = "vez" if quantidade == 1 else "vezes"
            print(f"{posicao}º Lugar: {nome_proc} - Realizado {quantidade} {texto}")
        print("-" * 50)

    def mostra_relatorio_procedimentos_valores(self, procedimentos_ordenados):
        print("\n--- RELATÓRIO: PROCEDIMENTOS MAIS CAROS E MAIS BARATOS ---")
        if not procedimentos_ordenados:
            print("Nenhum procedimento registrado.")
            return
            
        nome_caro, valor_caro = procedimentos_ordenados[0]
        print(f"[MAIS CARO] -> Procedimento: {nome_caro} | Valor: R$ {valor_caro:.2f}")
        
        nome_barato, valor_barato = procedimentos_ordenados[-1]
        print(f"[MAIS BARATO] -> Procedimento: {nome_barato} | Valor: R$ {valor_barato:.2f}")
        
        print("\nRanking Completo:")
        for posicao, (nome_proc, valor) in enumerate(procedimentos_ordenados, start=1):
            print(f"{posicao}º - {nome_proc} - R$ {valor:.2f}")
        print("-" * 50)
            
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")