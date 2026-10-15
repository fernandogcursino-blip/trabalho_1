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

    def mostra_tela_opcoes(self):
        print("\n--- MENU DE ATENDIMENTOS ---")
        print("1 - Iniciar Novo Atendimento")
        print("2 - Alterar Atendimento")
        print("3 - Excluir Atendimento")
        print("4 - Adicionar Procedimento a um Atendimento")
        print("5 - Listar Atendimentos")
        print("6 - Registrar Pagamento (Integral ou Parcial)")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])


    def pega_dados_atendimento(self, pacientes, profissionais, tipos):
        print("\n--- DADOS DO ATENDIMENTO ---")
        codigo = self.le_num_inteiro("Código do Atendimento (número): ")
        data = input("Data (DD/MM/AAAA): ").strip()
        horario = input("Horário de Início (HH:MM): ").strip()
        horario_fim = input("Horário de Fim (HH:MM): ").strip()
        
        while True:
            valor_str = input("Valor Base (R$): ").strip().replace(',', '.')
            try:
                valor_base = float(valor_str)
                break
            except ValueError:
                print("Valor inválido.")

        print("\n--- SELECIONE O TIPO DE ATENDIMENTO ---")
        for i, t in enumerate(tipos):
            print(f"[{i}] {t.nome} - {t.descricao}")
        idx_tipo = self.le_num_inteiro("Número do Tipo: ", list(range(len(tipos))))
        tipo_escolhido = tipos[idx_tipo]

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
            "codigo": codigo, "paciente": paciente_escolhido, "profissional": profissional_escolhido,
            "data": data, "horario": horario, "horario_fim": horario_fim,
            "tipo_atendimento": tipo_escolhido, "valor_base": valor_base
        }

    def pega_dados_procedimento(self):
        print("\n--- DADOS DO PROCEDIMENTO ---")
        nome = input("Nome do procedimento: ").strip()
        while True:
            valor_str = input("Valor do procedimento (R$): ").strip().replace(',', '.')
            try:
                valor = float(valor_str)
                break
            except ValueError:
                print("Valor inválido.")
        return {"nome": nome, "valor": valor}

    def pega_dados_pagamento(self, valor_restante):
        print(f"\n--- REGISTRAR NOVO PAGAMENTO ---")
        print(f"Valor RESTANTE a pagar neste atendimento: R$ {valor_restante:.2f}")
        data = input("Data do pagamento (DD/MM/AAAA): ").strip()
        while True:
            valor_str = input("Valor a pagar (R$): ").strip().replace(',', '.')
            try:
                valor_pago = float(valor_str)
                if valor_pago <= 0:
                    print("Erro: O valor pago deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Valor inválido.")

        print("\nModalidade de Pagamento:\n1 - Dinheiro\n2 - PIX\n3 - Cartão de Crédito")
        tipo = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3])
        cpf_pagador = input("CPF do Pagador: ").strip() if tipo == 2 else None
        numero_cartao = input("Número do Cartão: ").strip() if tipo == 3 else None
        bandeira = input("Bandeira: ").strip() if tipo == 3 else None

        return {"data": data, "valor_pago": valor_pago, "tipo": tipo, "cpf_pagador": cpf_pagador, "numero_cartao": numero_cartao, "bandeira": bandeira}

    def mostra_atendimentos(self, atendimentos):
        print("\n--- LISTA DE ATENDIMENTOS ---")
        for a in atendimentos:
            codigo = a.codigo if hasattr(a, 'codigo') else 'N/A'
            data = a.data if hasattr(a, 'data') else 'N/A'
            status = a.status_pagamento if hasattr(a, 'status_pagamento') else 'Pendente'
            

            obj_tipo = a.tipo_atendimento if hasattr(a, 'tipo_atendimento') else None
            nome_tipo = obj_tipo.nome if hasattr(obj_tipo, 'nome') else obj_tipo
            
            valor_base = a.valor_base if hasattr(a, 'valor_base') else 0.0
            try: valor_total = a.calcula_valor_total()
            except: valor_total = valor_base
            try: valor_restante = a.calcula_valor_restante()
            except: valor_restante = valor_base
            
            procedimentos = a.procedimentos if hasattr(a, 'procedimentos') else []
            pagamentos = a.pagamentos if hasattr(a, 'pagamentos') else []
            
            print(f"\nCódigo: {codigo} | Data: {data} | Tipo: {nome_tipo} | Status: [{status.upper()}]")
            print(f"Paciente: {a.paciente.nome} | Profissional: {a.profissional.nome}")
            print(f"Valor Base (Consulta): R$ {float(valor_base):.2f}")
            print(f"Valor Total: R$ {float(valor_total):.2f} | Restante a Pagar: R$ {float(valor_restante):.2f}")
            
            if procedimentos:
                for p in procedimentos:
                    print(f"  - {p.nome}: R$ {float(p.valor):.2f}")
            if pagamentos:
                for pag in pagamentos:
                    print(f"  - Em {pag.data}: R$ {float(pag.valor_pago):.2f} [{pag.detalhe()}]")
            print("-" * 40)

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")