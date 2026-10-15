class TelaTipoAtendimento:
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

    def mostra_tela_opcoes(self):
        print("\n--- TIPOS DE ATENDIMENTO ---")
        print("1 - Incluir Tipo de Atendimento")
        print("2 - Alterar Tipo de Atendimento")
        print("3 - Excluir Tipo de Atendimento")
        print("4 - Listar Tipos de Atendimento")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_dados_tipo(self):
        print("\n--- DADOS DO TIPO DE ATENDIMENTO ---")
        codigo = self.le_num_inteiro("Código numérico: ")
        nome = input("Nome (ex: Consulta, Exame de Sangue, Retorno): ").strip()
        descricao = input("Descrição detalhada: ").strip()
        return {"codigo": codigo, "nome": nome, "descricao": descricao}

    def mostra_tipos(self, tipos):
        print("\n--- LISTA DE TIPOS DE ATENDIMENTO ---")
        for t in tipos:
            print(f"Código: {t.codigo} | Nome: {t.nome} | Descrição: {t.descricao}")
        print("-" * 40)

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")