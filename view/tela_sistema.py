class TelaSistema:
    def __init__(self, controlador):
        self._controlador = controlador

    def le_num_inteiro(self, mensagem: str = "", inteiros_validos: list = None):
        """Lê um número inteiro com validação."""
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numérico inteiro válido.")
                if inteiros_validos:
                    print(f"Valores válidos: {inteiros_validos}")

    def mostra_opcoes(self):
        print("\n" + "="*30)
        print("--- SISTEMA DA CLÍNICA ---")
        print("="*30)
        print("1 - Cadastrar Clínicas")
        print("2 - Cadastrar Profissionais")
        print("3 - Cadastrar Pacientes")
        print("4 - Gerenciar Atendimentos")
        print("5 - Relatórios")
        print("0 - Encerrar Sistema")
        print("="*30)
        
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")