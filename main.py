from agenda.Agenda import Agenda

agenda = Agenda()

dados = {}
dados['loja'] = 'Lojas XYZ'
dados['cnpj'] = '123456879'
dados['inicio_dia'] = '20'
dados['inicio_mes'] = '4'
dados['inicio_ano'] = '2022'
dados['inicio_hora'] = '8'
dados['inicio_minuto'] = '30'
dados['erp'] = 'ERP1'
dados['tempo_estimado'] = 60
dados['projeto'] = 'projeto'
dados['objetivo'] = 'Manutenção'
dados['responsavel'] = 'José da Silva'

agenda.adicionar_agendamento(**dados)

# Adicionar diversas Integrações em horários diversos
dados['objetivo'] = 'Integração'
dados['tempo_estimado'] = 180
dados['inicio_hora'] = 8
for dia in range(16, 21):
    dados['loja'] = 'Nova Loja dia ' + str(dia)
    dados['inicio_dia'] = dia
    agenda.adicionar_agendamento(**dados)

# Adicionar diversas manutenções em dias e horários diversos
dados['loja'] = 'Lojas ABC'
dados['objetivo'] = 'Manutenção'
for dia in range(3, 7):
    for hora in range(8, 11):
        dados['inicio_dia'] = dia
        dados['inicio_hora'] = hora
        agenda.adicionar_agendamento(**dados)

# Adicionar diversas manutenções em um mesmo horário

dados['objetivo'] = 'Manutenção'
dados['inicio_dia'] = 10
dados['inicio_mes'] = 5
dados['inicio_hora'] = 14
dados['inicio_minutos'] = 30
for loja in range(15):
    dados['loja'] = 'Loja ' + str(loja + 1) + ' manutencao '
    agenda.adicionar_agendamento(**dados)

# Esperado NappError por estourar o limite de 15
# agenda.adicionar_agendamento(**dados)

# Filtros
agenda.filtro_por_data_hora(20, 4, 2022, 8, 35)
agenda.filtro_por_data_hora(20, 4, 2022, 15, 35)
agenda.filtro_por_data_hora(4, 4, 2022, 8, 35)
agenda.filtro_por_objetivo('Manutenção')
agenda.filtro_por_objetivo('Integração')
agenda.filtro_por_data_hora(10, 5, 2022, 14, 30)

# Adicionar Limite de Regras para um determinado horário
# Hipoteticamente, 17/05/2022 15:30 teremos NappAcademy e vamos
# reduzir o limite de atendimento para no máximo 7 atendimentos.
agenda.adicionar_regra(17, 5, 2022, 15, 30, 4, 5, 7)
dados['objetivo'] = 'Manutenção'
dados['inicio_dia'] = 17
dados['inicio_mes'] = 5
dados['inicio_hora'] = 15
dados['inicio_minutos'] = 30
for loja in range(7):
    dados['loja'] = 'Loja ' + str(loja + 1) + ' manutencao '
    agenda.adicionar_agendamento(**dados)
# Verificando se temos 7 atendimento
agenda.filtro_por_data_hora(17, 5, 2022, 15, 30)
# Descomente e teremos um NappError
# agenda.adicionar_agendamento(**dados)