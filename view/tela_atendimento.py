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
        print("6 - Registrar Pagamento (Integral ou Parcial)")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])

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
            "codigo": codigo, "paciente": paciente_escolhido, "profissional": profissional_escolhido,
            "data": data, "horario": horario, "horario_fim": horario_fim,
            "tipo_atendimento": tipo_atendimento, "valor_base": valor_base
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
                print("Valor inválido. Digite um número.")
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
                print("Valor inválido. Digite um número.")

        print("\nModalidade de Pagamento:")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão de Crédito")
        tipo = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3])

        cpf_pagador = None
        numero_cartao = None
        bandeira = None

        if tipo == 2:
            cpf_pagador = input("CPF do Pagador: ").strip()
        elif tipo == 3:
            numero_cartao = input("Número do Cartão: ").strip()
            bandeira = input("Bandeira (ex: Visa, Mastercard): ").strip()

        return {
            "data": data, "valor_pago": valor_pago, "tipo": tipo,
            "cpf_pagador": cpf_pagador, "numero_cartao": numero_cartao, "bandeira": bandeira
        }

    def mostra_atendimentos(self, atendimentos):
        print("\n--- LISTA DE ATENDIMENTOS ---")
        for a in atendimentos:
            codigo = a.codigo if hasattr(a, 'codigo') else getattr(a, '_codigo', 'N/A')
            data = a.data if hasattr(a, 'data') else getattr(a, '_data', 'N/A')
            tipo = a.tipo_atendimento if hasattr(a, 'tipo_atendimento') else getattr(a, '_tipo_atendimento', 'N/A')
            status = a.status_pagamento if hasattr(a, 'status_pagamento') else 'Pendente'
            
            # Extrai o valor base sempre com fallback seguro
            valor_base = a.valor_base if hasattr(a, 'valor_base') else getattr(a, '_valor_base', 0.0)
            
            # Se o Python falhar em achar o cálculo, assumimos que o total é o próprio valor base
            try:
                valor_total = a.calcula_valor_total()
            except Exception:
                valor_total = valor_base
                
            try:
                valor_restante = a.calcula_valor_restante()
            except Exception:
                valor_restante = valor_base
            
            procedimentos = a.procedimentos if hasattr(a, 'procedimentos') else getattr(a, '_procedimentos', [])
            pagamentos = a.pagamentos if hasattr(a, 'pagamentos') else getattr(a, '_pagamentos', [])
            
            print(f"\nCódigo: {codigo} | Data: {data} | Tipo: {tipo} | Status: [{status.upper()}]")
            print(f"Paciente: {a.paciente.nome} | Profissional: {a.profissional.nome}")
            
            # Apresentação CLARA dos três valores financeiros
            print(f"Valor Base (Consulta): R$ {float(valor_base):.2f}")
            print(f"Valor Total (c/ Procedimentos): R$ {float(valor_total):.2f} | Restante a Pagar: R$ {float(valor_restante):.2f}")
            
            if procedimentos:
                print("Procedimentos adicionais:")
                for p in procedimentos:
                    p_nome = p.nome if hasattr(p, 'nome') else getattr(p, '_nome', 'Desconhecido')
                    p_valor = p.valor if hasattr(p, 'valor') else getattr(p, '_valor', 0.0)
                    print(f"  - {p_nome}: R$ {float(p_valor):.2f}")
                    
            if pagamentos:
                print("Histórico de Pagamentos (Parcelas):")
                for pag in pagamentos:
                    p_data = pag.data if hasattr(pag, 'data') else getattr(pag, '_data', 'N/A')
                    p_valor = pag.valor_pago if hasattr(pag, 'valor_pago') else getattr(pag, '_valor_pago', 0.0)
                    try:
                        p_detalhe = pag.detalhe()
                    except:
                        p_detalhe = "N/A"
                    print(f"  - Em {p_data}: R$ {float(p_valor):.2f} [{p_detalhe}]")
            print("-" * 40)

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")