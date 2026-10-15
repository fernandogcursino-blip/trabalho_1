class TelaAtendimento:
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
        print("\n--- MENU DE ATENDIMENTOS ---")
        print("1 - Iniciar Novo Atendimento")
        print("2 - Alterar Atendimento")
        print("3 - Excluir Atendimento")
        print("4 - Adicionar Procedimento a um Atendimento")
        print("5 - Listar Atendimentos")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])

    def pega_dados_atendimento(self, pacientes, profissionais):
        print("\n--- DADOS DO ATENDIMENTO ---")
        codigo = self.le_num_inteiro("Código do Atendimento (número): ")
        data = input("Data (DD/MM/AAAA): ").strip()
        horario = input("Horário de Início (HH:MM): ").strip()
        horario_fim = input("Horário de Fim (HH:MM): ").strip()
        tipo_atendimento = input("Tipo de Atendimento (ex: Consulta, Retorno, Exame): ").strip()
        
        while True:
            valor_str = input("Valor Base (R$): ").strip().replace(',', '.')
            try:
                valor_base = float(valor_str)
                break
            except ValueError:
                print("Valor inválido. Digite um número (ex: 150.50).")

        print("\n--- SELECIONE O PACIENTE ---")
        for i, p in enumerate(pacientes):
            print(f"[{i}] {p.nome} (CPF: {p.cpf})")
        idx_paciente = self.le_num_inteiro("Número do Paciente: ", list(range(len(pacientes))))
        paciente_escolhido = pacientes[idx_paciente]

        print("\n--- SELECIONE O PROFISSIONAL ---")
        for i, prof in enumerate(profissionais):
            print(f"[{i}] {prof.nome} - {prof.especialidade} (Clínica: {prof.clinica.nome})")
        idx_profissional = self.le_num_inteiro("Número do Profissional: ", list(range(len(profissionais))))
        profissional_escolhido = profissionais[idx_profissional]

        return {
            "codigo": codigo,
            "paciente": paciente_escolhido,
            "profissional": profissional_escolhido,
            "data": data,
            "horario": horario,
            "horario_fim": horario_fim,
            "tipo_atendimento": tipo_atendimento,
            "valor_base": valor_base
        }

    def pega_dados_procedimento(self):
        print("\n--- DADOS DO PROCEDIMENTO ---")
        nome = input("Nome do procedimento (ex: Consulta, Exame): ").strip()
        
        while True:
            valor_str = input("Valor do procedimento (R$): ").strip().replace(',', '.')
            try:
                valor = float(valor_str)
                break
            except ValueError:
                print("Valor inválido. Digite um número (ex: 150.50).")

        return {"nome": nome, "valor": valor}

    def mostra_atendimentos(self, atendimentos):
        print("\n--- LISTA DE ATENDIMENTOS ---")
        for a in atendimentos:
            codigo = a.codigo if hasattr(a, 'codigo') else a._codigo
            data = a.data if hasattr(a, 'data') else a._data
            tipo = a.tipo_atendimento if hasattr(a, 'tipo_atendimento') else getattr(a, '_tipo_atendimento', 'N/A')
            valor = a.valor_base if hasattr(a, 'valor_base') else getattr(a, '_valor_base', 0.0)
            
            procedimentos = a.procedimentos if hasattr(a, 'procedimentos') else getattr(a, '_procedimentos', [])
            
            print(f"\nCódigo: {codigo} | Data: {data} | Tipo: {tipo} | Valor Base: R$ {valor:.2f}")
            print(f"Paciente: {a.paciente.nome}")
            print(f"Profissional: {a.profissional.nome} ({a.profissional.especialidade})")
            
            if procedimentos:
                print("Procedimentos realizados:")
                for p in procedimentos:
                    nome_proc = p.nome if hasattr(p, 'nome') else p._nome
                    valor_proc = p.valor if hasattr(p, 'valor') else p._valor
                    print(f"  - {nome_proc}: R$ {valor_proc:.2f}")
            else:
                print("Procedimentos: Nenhum procedimento registrado.")
            print("-" * 30)

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")