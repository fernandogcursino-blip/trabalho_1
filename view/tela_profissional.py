class TelaProfissional:
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
        print("\n--- MENU DE PROFISSIONAIS ---")
        print("1 - Incluir Profissional")
        print("2 - Alterar Profissional")
        print("3 - Excluir Profissional")
        print("4 - Listar Profissionais")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_dados_profissional(self, clinicas_disponiveis):
        print("\n--- DADOS DO PROFISSIONAL ---")
        nome = input("Nome: ").strip()
        celular = input("Celular: ").strip()
        cpf = input("CPF: ").strip()
        especialidade = input("Especialidade: ").strip()
        registro = input("Registro Profissional: ").strip()
        
        if not nome or not celular or not cpf or not especialidade or not registro:
            print("Erro: Todos os campos são obrigatórios.")
            return None

        print("\n--- SELECIONE A CLÍNICA DO PROFISSIONAL ---")
        for i, c in enumerate(clinicas_disponiveis):
            # Acessa os atributos usando as propriedades da classe Clinica
            print(f"[{i}] {c.nome} (CNPJ: {c.cnpj})")
            
        opcoes_validas = list(range(len(clinicas_disponiveis)))
        idx_clinica = self.le_num_inteiro("Escolha o número da Clínica: ", opcoes_validas)
        clinica_escolhida = clinicas_disponiveis[idx_clinica]
            
        return {
            "nome": nome, 
            "celular": celular, 
            "cpf": cpf, 
            "especialidade": especialidade, 
            "registro_profissional": registro,
            "clinica": clinica_escolhida
        }

    def pega_cpf(self, mensagem="Digite o CPF do profissional: "):
        return input(f"\n{mensagem}").strip()

    def mostra_profissionais(self, profissionais):
        print("\n--- LISTA DE PROFISSIONAIS ---")
        for p in profissionais:
            # Mostra também o nome da clínica vinculada
            print(f"Nome: {p.nome} | CPF: {p.cpf} | Esp: {p.especialidade} | Clínica: {p.clinica.nome}")
            
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")