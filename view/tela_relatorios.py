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
        # Pode adicionar os prints dos outros relatórios aqui
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1])

    def mostra_relatorio_clinicas(self, clinicas_ordenadas):
        print("\n--- RELATÓRIO: CLÍNICAS COM MAIS ATENDIMENTOS ---")
        # Enumerate ajuda a criar a numeração do ranking (1º, 2º, 3º...)
        for posicao, (nome_clinica, quantidade) in enumerate(clinicas_ordenadas, start=1):
            texto_atendimento = "atendimento" if quantidade == 1 else "atendimentos"
            print(f"{posicao}º Lugar: {nome_clinica} - {quantidade} {texto_atendimento}")
        print("-" * 50)
            
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")