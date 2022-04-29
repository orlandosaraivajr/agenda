from agenda.Agendamento import Agendamento
from agenda.Agendamento import NappError
from .Agenda import Agenda
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


class TestAgenda:
    def test_class_declared(self):
        objeto = Agenda()
        assert isinstance(objeto, Agenda)
        assert isinstance(objeto.agendamentos, list)

    def test_metodo_adicionar_agendamento(self):
        objeto = Agenda()
        assert len(objeto.agendamentos) == 0
        objeto.adicionar_agendamento(**dados)
        assert len(objeto.agendamentos) == 1
        assert isinstance(objeto.agendamentos[0], Agendamento)

    def test_metodo_adicionar_agendamento_2(self):
        objeto = Agenda()
        assert len(objeto.agendamentos) == 0
        for i in range(10):
            dados['loja'] = 'Loja ' + str(i)
            objeto.adicionar_agendamento(**dados)
        assert len(objeto.agendamentos) == 10

    def test_metodo_adicionar_agendamento_fail(self):
        objeto = Agenda()
        assert len(objeto.agendamentos) == 0
        msg = 'Extrapolou o limite de 15 agendamentos'
        for i in range(15):
            dados['loja'] = 'Loja ' + str(i)
            objeto.adicionar_agendamento(**dados)
        with pytest.raises(NappError) as error:
            objeto.adicionar_agendamento(**dados)
        assert str(error.value) == msg

    def test_metodo_adicionar_regras(self):
        objeto = Agenda()
        assert len(objeto.regras) == 0
        objeto.adicionar_regra(10, 5, 2022, 9, 30, 5, 7, 10)
        assert len(objeto.regras) == 1

    def test_metodo_consultar_regra(self):
        objeto = Agenda()
        assert len(objeto.regras) == 0
        regras = objeto.consultar_regra(10, 5, 2022, 9, 30)
        assert regras[0] == 15
        assert regras[1] == 13
        assert regras[2] == 10
        objeto.adicionar_regra(10, 5, 2022, 9, 30, 5, 7, 10)
        regras = objeto.consultar_regra(10, 5, 2022, 9, 30)
        assert regras[0] == 10
        assert regras[1] == 7
        assert regras[2] == 5

    def test_metodo_filtro_por_data_hora(self):
        objeto = Agenda()
        assert len(objeto.agendamentos) == 0
        for loja in range(1, 6):
            for hora in range(8, 11):
                dados['loja'] = 'Loja ' + str(loja)
                dados['inicio_hora'] = hora
                objeto.adicionar_agendamento(**dados)
        assert len(objeto.agendamentos) == 15
        filtrado = objeto.filtro_por_data_hora(20, 4, 2022, 8, 30)
        assert len(filtrado) == 5

    def test_metodo_filtro_por_data_hora_2(self):
        objeto = Agenda()
        assert len(objeto.agendamentos) == 0
        for loja in range(1, 6):
            for hora in range(8, 11):
                dados['loja'] = 'Loja ' + str(loja)
                dados['inicio_hora'] = hora
                objeto.adicionar_agendamento(**dados)
        assert len(objeto.agendamentos) == 15
        filtrado = objeto.filtro_por_data_hora(20, 4, 2022, 20, 0)
        assert len(filtrado) == 0

    def test_metodo_filtro_objetivo(self):
        objeto = Agenda()
        assert len(objeto.agendamentos) == 0
        for loja in range(10):
            dados['loja'] = 'Lojas ABC ' + str(loja)
            objeto.adicionar_agendamento(**dados)
        dados['objetivo'] = 'Integração'
        for loja in range(5):
            dados['loja'] = 'Lojas XYZ ' + str(loja)
            objeto.adicionar_agendamento(**dados)
        assert len(objeto.agendamentos) == 15
        assert len(objeto.filtro_por_objetivo('Integração')) == 5
        assert len(objeto.filtro_por_objetivo('Manutenção')) == 10

    def test_metodo_filtro_objetivo_2(self):
        objeto = Agenda()
        assert len(objeto.agendamentos) == 0
        for loja in range(15):
            dados['loja'] = 'Lojas ABC ' + str(loja)
            objeto.adicionar_agendamento(**dados)
        assert len(objeto.agendamentos) == 15
        assert len(objeto.filtro_por_objetivo('Integração')) == 15
        assert len(objeto.filtro_por_objetivo('Manutenção')) == 0

    def test_metodo_adicionar_agendamento_fail_1(self):
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

    def test_str_repr(self):
        objeto = Agenda()
        msg = 'Agenda'
        assert str(objeto) == msg
        assert repr(objeto) == msg
