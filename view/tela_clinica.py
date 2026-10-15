class TelaClinica:
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
                print("Valor incorreto: Digite um valor numérico inteiro válido.")
                if inteiros_validos:
                    print(f"Valores válidos: {inteiros_validos}")

    def mostra_tela_opcoes(self):
        print("\n--- MENU DE CLÍNICAS ---")
        print("1 - Incluir Clínica")
        print("2 - Alterar Clínica")
        print("3 - Excluir Clínica")
        print("4 - Listar Clínicas")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_dados_clinica(self):
        print("\n--- DADOS DA CLÍNICA ---")
        nome = input("Nome da Clínica: ").strip()
        cnpj = input("CNPJ: ").strip()
        endereco = input("Endereço: ").strip()
        horario_abertura = input("Horário de Abertura (ex: 08:00): ").strip()
        horario_fechamento = input("Horário de Fechamento (ex: 18:00): ").strip()
        
        if not nome or not cnpj or not endereco or not horario_abertura or not horario_fechamento:
            print("Erro: Todos os campos são obrigatórios.")
            return None
            
        return {
            "nome": nome, 
            "cnpj": cnpj, 
            "endereco": endereco,
            "horario_abertura": horario_abertura,
            "horario_fechamento": horario_fechamento
        }

    def pega_cnpj(self, mensagem="Digite o CNPJ da clínica: "):
        return input(f"\n{mensagem}").strip()

    def mostra_clinicas(self, clinicas):
        print("\n--- LISTA DE CLÍNICAS ---")
        for clinica in clinicas:
            print(f"Nome: {clinica._nome} | CNPJ: {clinica._cnpj} | Endereço: {clinica._endereco} | Horários: {clinica._horario_abertura} às {clinica._horario_fechamento}")
            
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")