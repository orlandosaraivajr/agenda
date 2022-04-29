from .Agendamento import Agendamento, NappError
from .Setup import Setup

class Agenda:
    def __init__(self):
        self._agendamentos = []
        self._configuracoes = Setup()

    @property
    def agendamentos(self):
        return self._agendamentos

    @property
    def regras(self):
        return self._configuracoes._regras

    def adicionar_agendamento(self, **kwargs):
        Agendamento.verificar_campos_obrigatorios(**kwargs)
        dia, mes, ano, hora, minuto = Agendamento.extrair_parametros_data(**kwargs)
        quantidade_agendada = len(self.filtro_por_data_hora(dia, mes, ano, hora, minuto))
        limite_agendamento = self._configuracoes.limite_agendamento(dia, mes, ano, hora, minuto)
        if quantidade_agendada < limite_agendamento :
            self.agendamentos.append(Agendamento(**kwargs))
        else:
            error = 'Extrapolou o limite de '
            error += str(limite_agendamento) + ' agendamentos'
            raise NappError(error)

    def adicionar_regra(self, dia, mes, ano, hora, minuto, limite_verde, limite_amarelo, limite_vermelho):
        self._configuracoes.adicionar_regra(dia, mes, ano, hora, minuto, limite_verde, limite_amarelo, limite_vermelho)

    def consultar_regra(self, dia, mes, ano, hora, minuto):
        return self._configuracoes.consultar_regra(dia, mes, ano, hora, minuto)

    def filtro_por_data_hora(self, dia, mes, ano, hora, minuto):
        match = []
        for agendamento in self.agendamentos:
            if agendamento.filtro_horario(dia, mes, ano, hora, minuto):
                match.append(agendamento)
        return match

    def filtro_por_objetivo(self, objetivo):
        match = []
        for agendamento in self.agendamentos:
            if agendamento.filtro_objetivo(objetivo):
                match.append(agendamento)
        return match

    def __str__(self):
        mensagem = 'Agenda'
        return mensagem

    def __repr__(self):
        return str(self)
