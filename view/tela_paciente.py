class TelaPaciente:
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
        print("\n--- MENU DE PACIENTES ---")
        print("1 - Incluir Paciente")
        print("2 - Alterar Paciente")
        print("3 - Excluir Paciente")
        print("4 - Listar Pacientes")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_dados_paciente(self):
        print("\n--- DADOS DO PACIENTE ---")
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        idade = self.le_num_inteiro("Idade: ")
        telefone = input("Telefone: ").strip()
        
        if not nome or not cpf or not telefone:
            print("Erro: Nome, CPF e Telefone são obrigatórios.")
            return None
            
        return {"nome": nome, "cpf": cpf, "idade": idade, "telefone": telefone}

    def pega_cpf(self, mensagem="Digite o CPF do paciente: "):
        return input(f"\n{mensagem}").strip()

    def mostra_pacientes(self, pacientes):
        print("\n--- LISTA DE PACIENTES ---")
        for p in pacientes:
            nome = p.nome if hasattr(p, 'nome') else p._nome
            cpf = p.cpf if hasattr(p, 'cpf') else p._cpf
            # Fallback seguro para atributos que podem não ter getters configurados
            idade = p.idade if hasattr(p, 'idade') else getattr(p, '_idade', 'N/A')
            telefone = p.telefone if hasattr(p, 'telefone') else getattr(p, '_telefone', 'N/A')
            
            print(f"Nome: {nome} | CPF: {cpf} | Idade: {idade} | Tel: {telefone}")
            
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")