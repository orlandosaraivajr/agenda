from .Agendamento import Agendamento


class Setup:
    def __init__(self):
        self._limite_cor_verde = 10
        self._limite_cor_amarela = 13
        self._limite_cor_vermelha = 15
        self._regras = []

    def limite_agendamento(self, dia, mes, ano, hora, minuto):
        regra_cadastrada = self.consultar_regra(dia, mes, ano, hora, minuto)
        return regra_cadastrada[0]

    def adicionar_regra(self, dia, mes, ano, hora, minuto, limite_verde, limite_amarelo, limite_vermelho):
        regra = (dia, mes, ano, hora, minuto, limite_verde, limite_amarelo, limite_vermelho)
        self._regras.append(regra)

    def consultar_regra(self, dia, mes, ano, hora, minuto):
        """ Retornar tupla (limite_vermelho, limite_amarelo, limite_verde) """
        for regra in self._regras:
            if regra[0] == dia and regra[1] == mes and regra[2] == ano:
                if regra[3] == hora and regra[4] == minuto:
                    return (regra[7], regra[6], regra[5])
        return (self._limite_cor_vermelha, self._limite_cor_amarela, self._limite_cor_verde)

    def __str__(self):
        return 'Central de Regras para o agendamento'

    def __repr__(self):
        return str(self)
