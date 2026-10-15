from datetime import datetime

class TelaPaciente:
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

    def mostra_tela_opcoes(self):
        """Mostra o menu e retorna a opção escolhida."""
        print("\n--- CADASTRO DE PACIENTES ---")
        print("1 - Incluir Paciente")
        print("2 - Alterar Paciente")
        print("3 - Excluir Paciente")
        print("4 - Listar Pacientes")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_dados_paciente(self):
        """Solicita os dados para cadastro e retorna um dicionário."""
        print("\n--- DADOS DO PACIENTE ---")
        nome = input("Nome: ").strip()
        celular = input("Celular: ").strip()
        cpf = input("CPF: ").strip()
        
        # Aplicando a mesma lógica de repetição do le_num_inteiro para a data
        while True:
            data_nascimento_str = input("Data de Nascimento (DD/MM/AAAA): ").strip()
            try:
                data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Erro: Data em formato inválido! Utilize o formato DD/MM/AAAA.")

        return {
            "nome": nome, 
            "celular": celular, 
            "cpf": cpf, 
            "data_nascimento": data_nascimento
        }

    def pega_cpf(self, mensagem="CPF do Paciente: "):
        """Pede ao utilizador um CPF (string)."""
        return input(mensagem).strip()

    def mostra_pacientes(self, pacientes):
        """Exibe a lista de pacientes."""
        print("\n=== Lista de Pacientes ===")
        for paciente in pacientes:
            print(paciente)

    def mostra_mensagem(self, mensagem):
        """Exibe uma mensagem."""
        print(f"\n{mensagem}")