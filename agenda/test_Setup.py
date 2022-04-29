from agenda.Setup import Setup
from agenda.Agendamento import NappError
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


class TestSetup:
    def test_class_declared(self):
        objeto = Setup()
        assert isinstance(objeto, Setup)
        assert isinstance(objeto._limite_cor_verde, int)
        assert isinstance(objeto._limite_cor_amarela, int)
        assert isinstance(objeto._limite_cor_vermelha, int)
        assert isinstance(objeto._regras, list)

    def test_default_values(self):
        objeto = Setup()
        assert isinstance(objeto, Setup)
        assert objeto._limite_cor_verde == 10
        assert objeto._limite_cor_amarela == 13
        assert objeto._limite_cor_vermelha == 15
        assert objeto._regras == []

    def test_metodo_adicionar_regra(self):
        objeto = Setup()
        assert len(objeto._regras) == 0
        assert objeto.limite_agendamento(15, 5, 2022, 8, 30) == 15
        objeto.adicionar_regra(15, 5, 2022, 8, 30, 5, 8, 10)
        assert objeto.limite_agendamento(15, 5, 2022, 8, 30) == 10
        assert len(objeto._regras) == 1
        
    def test_str_repr(self):
        objeto = Setup()
        msg = 'Central de Regras para o agendamento'
        assert str(objeto) == msg
        assert repr(objeto) == msg
