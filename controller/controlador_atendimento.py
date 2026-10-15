from view.tela_atendimento import TelaAtendimento
from model import Atendimento, Procedimento
from model.pagamento import PagamentoDinheiro, PagamentoPix, PagamentoCartao
from datetime import datetime

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self._tela_atendimento = TelaAtendimento(self)
        self._controlador_sistema = controlador_sistema
        self._atendimentos = []

    @property
    def atendimentos(self):
        return self._atendimentos

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_atendimento(self):
        pacientes = self._controlador_sistema._controlador_paciente.pacientes
        profissionais = self._controlador_sistema._controlador_profissional.profissionais
        
        if not pacientes or not profissionais:
            self._tela_atendimento.mostra_mensagem("Erro: É preciso ter pelo menos 1 Paciente e 1 Profissional cadastrados!")
            return

        dados = self._tela_atendimento.pega_dados_atendimento(pacientes, profissionais)
        if not dados:
            return
            
        if self.__atendimento_existe(dados['codigo']):
            self._tela_atendimento.mostra_mensagem("Erro: Já existe um atendimento com este código.")
            return
            
        try:
            novo_atendimento = Atendimento(
                dados['codigo'], dados['paciente'], dados['profissional'], 
                dados['data'], dados['horario'], dados['horario_fim'],
                dados['tipo_atendimento'], dados['valor_base']
            )
            self._atendimentos.append(novo_atendimento)
            self._tela_atendimento.mostra_mensagem("\n✅ Atendimento agendado com sucesso!")
            
        except ValueError as e:
            mensagem_erro = f"\n======================================================\n❌ AGENDAMENTO CANCELADO (HORÁRIO):\n{e}\n======================================================"
            self._tela_atendimento.mostra_mensagem(mensagem_erro)
        except Exception as e:
            # Captura a PacienteMenorDeIdadeException e exibe em formato de destaque
            mensagem_erro = f"\n======================================================\n❌ AGENDAMENTO RECUSADO (REGRAS DA CLÍNICA):\n{e}\n======================================================"
            self._tela_atendimento.mostra_mensagem(mensagem_erro)

    def altera_atendimento(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        codigo = self._tela_atendimento.le_num_inteiro("Digite o código do atendimento que deseja alterar: ")
        
        atendimento_encontrado = None
        indice = -1
        for i, a in enumerate(self._atendimentos):
            codigo_atual = a.codigo if hasattr(a, 'codigo') else a._codigo
            if codigo_atual == codigo:
                atendimento_encontrado = a
                indice = i
                break
                
        if not atendimento_encontrado:
            self._tela_atendimento.mostra_mensagem("Atendimento não encontrado.")
            return

        pacientes = self._controlador_sistema._controlador_paciente.pacientes
        profissionais = self._controlador_sistema._controlador_profissional.profissionais
        
        self._tela_atendimento.mostra_mensagem("Insira os novos dados do atendimento:")
        novos_dados = self._tela_atendimento.pega_dados_atendimento(pacientes, profissionais)
        if not novos_dados:
            return
            
        try:
            atendimento_atualizado = Atendimento(
                novos_dados['codigo'], novos_dados['paciente'], novos_dados['profissional'], 
                novos_dados['data'], novos_dados['horario'], novos_dados['horario_fim'],
                novos_dados['tipo_atendimento'], novos_dados['valor_base']
            )
            
            if hasattr(atendimento_atualizado, '_procedimentos'):
                atendimento_atualizado._procedimentos = atendimento_encontrado.procedimentos
            if hasattr(atendimento_atualizado, '_pagamentos'):
                atendimento_atualizado._pagamentos = atendimento_encontrado.pagamentos
                
            self._atendimentos[indice] = atendimento_atualizado
            self._tela_atendimento.mostra_mensagem("\n✅ Atendimento alterado com sucesso!")
            
        except ValueError as e:
            mensagem_erro = f"\n======================================================\n❌ ALTERAÇÃO CANCELADA (HORÁRIO):\n{e}\n======================================================"
            self._tela_atendimento.mostra_mensagem(mensagem_erro)
        except Exception as e:
            mensagem_erro = f"\n======================================================\n❌ ALTERAÇÃO RECUSADA (REGRAS DA CLÍNICA):\n{e}\n======================================================"
            self._tela_atendimento.mostra_mensagem(mensagem_erro)

    def exclui_atendimento(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        codigo = self._tela_atendimento.le_num_inteiro("Digite o código do atendimento a excluir: ")
        
        for i, a in enumerate(self._atendimentos):
            codigo_atual = a.codigo if hasattr(a, 'codigo') else a._codigo
            if codigo_atual == codigo:
                del self._atendimentos[i]
                self._tela_atendimento.mostra_mensagem(f"Atendimento {codigo} excluído com sucesso!")
                return
                
        self._tela_atendimento.mostra_mensagem("Atendimento não encontrado.")

    def adiciona_procedimento_no_atendimento(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        codigo = self._tela_atendimento.le_num_inteiro("Código do Atendimento: ")
        atendimento_encontrado = None
        for a in self._atendimentos:
            codigo_atual = a.codigo if hasattr(a, 'codigo') else a._codigo
            if codigo_atual == codigo:
                atendimento_encontrado = a
                break
                
        if not atendimento_encontrado:
            self._tela_atendimento.mostra_mensagem("Atendimento não encontrado.")
            return
            
        dados_procedimento = self._tela_atendimento.pega_dados_procedimento()
        if dados_procedimento:
            novo_procedimento = Procedimento(
                dados_procedimento['nome'], dados_procedimento['valor'], atendimento_encontrado.profissional
            )
            atendimento_encontrado.adiciona_procedimento(novo_procedimento)
            self._tela_atendimento.mostra_mensagem("Procedimento adicionado com sucesso!")

    def realiza_pagamento(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        codigo = self._tela_atendimento.le_num_inteiro("Digite o código do atendimento para pagamento: ")
        
        atendimento_encontrado = None
        for a in self._atendimentos:
            codigo_atual = a.codigo if hasattr(a, 'codigo') else a._codigo
            if codigo_atual == codigo:
                atendimento_encontrado = a
                break
                
        if not atendimento_encontrado:
            self._tela_atendimento.mostra_mensagem("Atendimento não encontrado.")
            return
            
        valor_restante = atendimento_encontrado.calcula_valor_restante()
        
        if valor_restante <= 0:
            self._tela_atendimento.mostra_mensagem("Este atendimento já se encontra totalmente PAGO.")
            return
            
        dados_pag = self._tela_atendimento.pega_dados_pagamento(valor_restante)
        if not dados_pag:
            return

        try:
            data_pag_dt = datetime.strptime(dados_pag['data'], "%d/%m/%Y")
            data_atend_dt = datetime.strptime(atendimento_encontrado.data, "%d/%m/%Y")
            if data_pag_dt > data_atend_dt:
                self._tela_atendimento.mostra_mensagem("\n======================================================\n❌ ERRO DE PAGAMENTO:\nOs pagamentos devem ser realizados ATÉ a data do atendimento.\n======================================================")
                return
        except ValueError:
            self._tela_atendimento.mostra_mensagem("Erro: Formato de data inválido.")
            return

        valor_a_registrar = dados_pag['valor_pago']
        if valor_a_registrar > valor_restante:
            self._tela_atendimento.mostra_mensagem(f"Aviso: O valor excede o restante. Registrando apenas R$ {valor_restante:.2f}.")
            valor_a_registrar = valor_restante

        if dados_pag['tipo'] == 1:
            novo_pagamento = PagamentoDinheiro(
                dados_pag['data'], atendimento_encontrado, atendimento_encontrado.paciente, valor_a_registrar
            )
        elif dados_pag['tipo'] == 2:
            novo_pagamento = PagamentoPix(
                dados_pag['data'], atendimento_encontrado, atendimento_encontrado.paciente, valor_a_registrar, dados_pag['cpf_pagador']
            )
        elif dados_pag['tipo'] == 3:
            novo_pagamento = PagamentoCartao(
                dados_pag['data'], atendimento_encontrado, atendimento_encontrado.paciente, valor_a_registrar, dados_pag['numero_cartao'], dados_pag['bandeira']
            )

        atendimento_encontrado.adiciona_pagamento(novo_pagamento)
        self._tela_atendimento.mostra_mensagem("\n✅ Pagamento (parcela) registrado com sucesso!")

    def lista_atendimentos(self):
        if not self._atendimentos:
            self._tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        self._tela_atendimento.mostra_atendimentos(self._atendimentos)

    def retornar(self):
        return
    
    def abre_tela_inicial(self):
        switcher = {
            0: self.retornar, 1: self.inclui_atendimento, 2: self.altera_atendimento,
            3: self.exclui_atendimento, 4: self.adiciona_procedimento_no_atendimento,
            5: self.lista_atendimentos, 6: self.realiza_pagamento
        }
        while True:
            opcao = self._tela_atendimento.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao, lambda: self._tela_atendimento.mostra_mensagem("Opção inválida"))
            funcao_escolhida()
            if opcao == 0:
                break

    def __atendimento_existe(self, codigo):
        for a in self._atendimentos:
            codigo_atual = a.codigo if hasattr(a, 'codigo') else a._codigo
            if codigo_atual == codigo: return True
        return False