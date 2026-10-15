from datetime import datetime

class TelaAtendimento:
    def __init__(self, controlador):
        self._controlador = controlador

    def mostra_tela_opcoes(self):
        print("\n--- MENU DE ATENDIMENTOS ---")
        print("1 - Agendar Atendimento")
        print("4 - Listar Atendimentos")
        print("0 - Retornar")
        
        try:
            return int(input("Escolha a opção: "))
        except ValueError:
            return -1

    def pega_dados_atendimento(self, pacientes, profissionais, clinicas):
        print("\n--- AGENDAR ATENDIMENTO ---")
        
        # Seleção da Clínica (Exemplo simplificado pegando a primeira, mas você pode iterar)
        print("\nClínicas disponíveis:")
        for i, c in enumerate(clinicas):
            print(f"{i} - {c._nome}")
        idx_clinica = int(input("Escolha o número da clínica: "))
        clinica_selecionada = clinicas[idx_clinica]

        # Seleção do Paciente
        print("\nPacientes disponíveis:")
        for i, p in enumerate(pacientes):
            print(f"{i} - {p.nome} (CPF: {p.cpf})")
        idx_pac = int(input("Escolha o número do paciente: "))
        paciente_selecionado = pacientes[idx_pac]

        # Seleção do Profissional
        print("\nProfissionais disponíveis:")
        for i, pr in enumerate(profissionais):
            print(f"{i} - {pr.nome} (Esp: {pr._especialidade})")
        idx_prof = int(input("Escolha o número do profissional: "))
        profissional_selecionado = profissionais[idx_prof]

        # Dados do agendamento
        data_str = input("\nData do Atendimento (DD/MM/AAAA): ")
        inicio_str = input("Horário de Início (HH:MM): ")
        fim_str = input("Horário de Término (HH:MM): ")
        tipo = input("Tipo de Atendimento (Consulta, Exame, etc): ")
        valor = float(input("Valor base (R$): "))

        try:
            data_atendimento = datetime.strptime(data_str, "%d/%m/%Y").date()
            horario_inicio = datetime.strptime(inicio_str, "%H:%M").time()
            horario_fim = datetime.strptime(fim_str, "%H:%M").time()
            
            return {
                "clinica": clinica_selecionada,
                "paciente": paciente_selecionado,
                "profissional": profissional_selecionado,
                "data": data_atendimento,
                "horario_inicio": horario_inicio,
                "horario_fim": horario_fim,
                "tipo": tipo,
                "valor_base": valor
            }
        except ValueError:
            print("Erro: Formato de data ou hora inválido!")
            return None

    def mostra_atendimentos(self, atendimentos):
        print("\n--- LISTA DE ATENDIMENTOS ---")
        for a in atendimentos:
            print(f"Data: {a._data_atendimento} | Paciente: {a._paciente.nome} | Profissional: {a._profissional.nome} | Clínica: {a._clinica._nome}")

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")