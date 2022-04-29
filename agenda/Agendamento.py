from datetime import datetime, timedelta


class NappError(Exception):
    pass


class Agendamento:
    def __init__(self, **kwargs):
        self.verificar_campos_obrigatorios(**kwargs)
        self.loja = kwargs['loja']
        self.cnpj = kwargs['cnpj']
        self.erp = kwargs['erp']
        self.dt1, self.dt2 = self._extrair_datetime(**kwargs)
        self.projeto = kwargs['projeto']
        self.responsavel = kwargs['responsavel']
        self.objetivo = kwargs['objetivo']

    @classmethod
    def verificar_campos_obrigatorios(self, **kwargs):
        campos_passados = set(kwargs.keys())
        campos_obrigatorios = ['loja', 'cnpj', 'erp', 'inicio_dia']
        campos_obrigatorios += ['inicio_mes', 'inicio_ano', 'inicio_hora']
        campos_obrigatorios += ['inicio_minuto', 'tempo_estimado', 'projeto']
        campos_obrigatorios += ['responsavel', 'objetivo']
        campos_obrigatorios = set(campos_obrigatorios)
        diferencas = campos_obrigatorios - campos_passados
        if len(diferencas) > 0:
            raise NappError('Campos não encontrados: ' + str(diferencas))

    @classmethod
    def extrair_parametros_data(self, **kwargs):
        ano = int(kwargs['inicio_ano'])
        mes = int(kwargs['inicio_mes'])
        dia = int(kwargs['inicio_dia'])
        hora = int(kwargs['inicio_hora'])
        minuto = int(kwargs['inicio_minuto'])
        return dia, mes, ano, hora, minuto

    def _extrair_datetime(self, **kwargs):
        dia, mes, ano, hora, minuto = Agendamento.extrair_parametros_data(**kwargs)
        dt1 = datetime(ano, mes, dia, hora, minuto)
        dt2 = dt1 + timedelta(minutes=int(kwargs['tempo_estimado']))
        return dt1, dt2

    def filtro_horario(self, dia, mes, ano, hora, minuto):
        data = datetime(ano, mes, dia, hora, minuto)
        return self.inicio_atendimento <= data <= self.termino_atendimento

    def filtro_objetivo(self, objetivo):
        if self.objetivo == objetivo:
            return True
        return False

    @property
    def atendimento(self):
        return self.loja

    @property
    def inicio_atendimento(self):
        return self.dt1

    @property
    def termino_atendimento(self):
        return self.dt2

    def __str__(self):
        mensagem = 'Agendamento ' + self.loja
        mensagem += ' Início: ' + str(self.dt1) + ' Fim: ' + str(self.dt2)
        return mensagem

    def __repr__(self):
        return str(self)
