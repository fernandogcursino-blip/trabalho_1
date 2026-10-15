class TelaSistema:
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
        print("\n" + "="*40)
        print("   SISTEMA DE GESTÃO DE CLÍNICAS   ")
        print("="*40)
        print("1 - Gerenciar Clínicas")
        print("2 - Gerenciar Profissionais")
        print("3 - Gerenciar Pacientes")
        print("4 - Gerenciar Tipos de Atendimento")
        print("5 - Gerenciar Atendimentos")
        print("6 - Emissão de Relatórios")
        print("0 - Encerrar Sistema")
        print("="*40)
        
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")