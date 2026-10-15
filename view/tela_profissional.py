class TelaProfissional:
    def __init__(self, controlador):
        self._controlador = controlador

    def mostra_tela_opcoes(self):
        print("\n--- MENU DE PROFISSIONAIS ---")
        print("1 - Incluir Profissional")
        # print("2 - Alterar Profissional")
        # print("3 - Excluir Profissional")
        print("4 - Listar Profissionais")
        print("0 - Retornar")
        
        try:
            return int(input("Escolha a opção: "))
        except ValueError:
            return -1

    def pega_dados_profissional(self):
        print("\n--- DADOS DO PROFISSIONAL ---")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro Profissional (CRM/Coren etc): ")
        
        return {
            "nome": nome, 
            "celular": celular, 
            "cpf": cpf, 
            "especialidade": especialidade,
            "registro_profissional": registro
        }

    def pega_cpf(self, mensagem="CPF do Profissional: "):
        return input(mensagem)

    def mostra_profissionais(self, profissionais):
        print("\n--- LISTA DE PROFISSIONAIS ---")
        for profissional in profissionais:
            print(profissional)

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")