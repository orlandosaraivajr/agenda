from datetime import datetime, timedelta
from .Agendamento import Agendamento, NappError
import pytest

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


class TestAgendamento:
    def test_class_declared(self):
        objeto = Agendamento(**dados)
        assert isinstance(objeto, Agendamento)

    def test_instanciar(self):
        objeto = Agendamento(**dados)
        assert isinstance(objeto, Agendamento)
        assert isinstance(objeto.loja, str)
        assert isinstance(objeto.cnpj, str)
        assert isinstance(objeto.erp, str)
        assert isinstance(objeto.inicio_atendimento, datetime)
        assert isinstance(objeto.termino_atendimento, datetime)
        assert isinstance(objeto.erp, str)
        assert isinstance(objeto.projeto, str)

    def test_instanciar_fail_1(self):
        dados = {}
        dados['loja'] = 'Lojas XYZ'
        dados['inicio_dia'] = '20'
        dados['inicio_mes'] = '4'
        dados['inicio_ano'] = '2022'
        dados['inicio_hora'] = '8'
        dados['inicio_minuto'] = '30'
        with pytest.raises(NappError) as error:
            Agendamento(**dados)
        assert 'Campos não encontrados' in str(error.value)
        assert 'cnpj' in str(error.value)

    def test_instanciar_fail_2(self):
        dados = {}
        dados['loja'] = 'Lojas XYZ'
        dados['cnpj'] = '123456879'
        dados['inicio_dia'] = '20'
        dados['inicio_mes'] = '4'
        dados['inicio_ano'] = '2022'
        dados['inicio_hora'] = '8'
        dados['inicio_minuto'] = '30'
        dados['erp'] = 'ERP1'
        dados['projeto'] = 'projeto'
        dados['objetivo'] = 'Manutenção'
        with pytest.raises(NappError) as error:
            Agendamento(**dados)
        assert 'Campos não encontrados' in str(error.value)
        assert 'responsavel' in str(error.value)
        assert 'tempo_estimado' in str(error.value)

    def test_metodo_filtro_horario(self):
        objeto = Agendamento(**dados)
        assert objeto.filtro_horario(20, 4, 2022, 8, 29) is False
        assert objeto.filtro_horario(20, 4, 2022, 8, 30)
        assert objeto.filtro_horario(20, 4, 2022, 9, 0)
        assert objeto.filtro_horario(20, 4, 2022, 9, 30)
        assert objeto.filtro_horario(20, 4, 2022, 9, 31) is False

    def test_metodo_filtro_objetivo(self):
        objeto = Agendamento(**dados)
        assert objeto.filtro_objetivo('Integração') is False
        assert objeto.filtro_objetivo('Manutenção')
        dados['objetivo'] = 'Integração'
        objeto2 = Agendamento(**dados)
        assert objeto2.filtro_objetivo('Integração')
        assert objeto2.filtro_objetivo('Manutenção') is False

    def test_properties(self):
        objeto = Agendamento(**dados)
        assert isinstance(objeto.loja, str)
        assert objeto.atendimento == 'Lojas XYZ'

    def test_properties_date(self):
        objeto = Agendamento(**dados)
        ano = int(dados['inicio_ano'])
        mes = int(dados['inicio_mes'])
        dia = int(dados['inicio_dia'])
        hora = int(dados['inicio_hora'])
        minuto = int(dados['inicio_minuto'])
        tempo_estimado = int(dados['tempo_estimado'])
        dt1 = datetime(ano, mes, dia, hora, minuto)
        dt2 = dt1 + timedelta(minutes=tempo_estimado)
        assert objeto.inicio_atendimento == dt1
        assert objeto.termino_atendimento == dt2

    def test_str_repr(self):
        objeto = Agendamento(**dados)
        msg = 'Agendamento Lojas XYZ '
        msg += 'Início: 2022-04-20 08:30:00 Fim: 2022-04-20 09:30:00'
        assert str(objeto) == msg
        assert repr(objeto) == msg
