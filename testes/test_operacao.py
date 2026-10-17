"""Seus testes do Marco 3 (veja a seção 5 do ENUNCIADO_MARCO3.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou math.isclose, a não
ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest

from elevatoria.raizes import Bisseccao
from elevatoria.raizes import Newton
from elevatoria.operacao import ordem_convergencia
from elevatoria.operacao import ponto_operacao
from elevatoria.calibracao import CurvaCalibracao
from fornecido.hidraulica import Tubulacao
import numpy as np


class TestBisseccaoExemplo(unittest.TestCase):
    """Exemplo do formato. `Bisseccao` é código existente da base."""

    def test_raiz_na_ponta(self):
        """Se f(a) já é zero, a bissecção devolve a sem iterar."""
        resultado = Bisseccao().encontrar(lambda x: x - 1.0, 1.0, 3.0)
        self.assertEqual((resultado.raiz, resultado.iteracoes), (1.0, 0))


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #9 (escreva-os ANTES de corrigir o defeito e confirme que falham).
class TesteNewton(unittest.TestCase):
    """Exemplo do formato. `Newton` é código existente da base."""

    def test_raiz_df(self):
        """Testa se o Newton converge para a raiz de f(x) = sin(x) com df(x) = cos(x). Issue #9."""
        resultado = Newton(df=lambda x: np.cos(x)).encontrar(lambda x: np.sin(x), -2.0, -0.01)
        self.assertAlmostEqual(resultado.raiz, 0.0, places=16)
        self.assertLessEqual(resultado.iteracoes, 6)

    def test_raiz_df_numerica(self):
        """Testa se o Newton converge para a raiz de f(x) = sin(x) com df(x) numérica. Issue #9."""
        resultado = Newton().encontrar(lambda x: np.sin(x), -2.0, -0.01)
        self.assertAlmostEqual(resultado.raiz, 0.0, places=16)
        self.assertLessEqual(resultado.iteracoes, 6)


class TesteOrdemConvergencia(unittest.TestCase):
    """Testa a função ordem_convergencia do módulo operacao.py."""

    def test_ordem_convergencia(self):
        """Testa se a função ordem_convergencia calcula 
        corretamente a ordem de convergência. Issue #8."""
        historico = [0.1, 0.01, 0.001, 0.0001]
        raiz = 0.0
        piso = 1e-5
        p = ordem_convergencia(historico, raiz, piso)
        self.assertAlmostEqual(p, 1.0, places=6)  

class TestePontoOperacao(unittest.TestCase):
    """Testa a função ponto_operacao do módulo operacao.py."""

    def test_ponto_operacao(self):
        """Testa se a função ponto_operacao calcula corretamente o ponto de operação. Issue #8."""

        # Criando uma curva de calibracao fictícia
        bomba = CurvaCalibracao(entradas=(10.0, 100.0, 190), saidas=[10.0, 0.0, -10.0])
        tubulacao = Tubulacao(diametro=.1, comprimento=100, rugosidade=.001, desnivel=1.0, resolvedor=Bisseccao())

        resolvedor = Bisseccao()
        ponto = ponto_operacao(bomba, tubulacao, resolvedor, a=10.0, b=190.0)

        self.assertAlmostEqual(ponto.vazao, 16.224688080, places=6)
        self.assertAlmostEqual(ponto.altura, 9.30836799, places=6)
        self.assertTrue(ponto.resultado.convergiu)

if __name__ == "__main__":
    unittest.main()
