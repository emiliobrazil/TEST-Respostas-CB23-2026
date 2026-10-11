"""Seus testes do Marco 2 (veja a seção 5 do ENUNCIADO_MARCO2.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual, math.isclose ou
np.allclose, a não ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest

from elevatoria.dados import ler_log, Registro
from elevatoria.medicao import Medicao, medir, altura_manometrica
from elevatoria.acumuladores import AcumuladorIngenuo

from elevatoria.calibracao import CurvaCalibracao

log_texto = """\
2026-10-05 08:00:00 INFO B1 evento=partida corrente=47.5
2026-10-05 08:00:00 INFO PT101 contagens=131
2026-10-05 08:00:00 INFO PT102 contagens=1790
2026-10-05 08:00:00 INFO FT201 pulsos=3873
2026-10-05 08:00:00 INFO LT301 nivel=46.99
2026-10-05 08:00:06 INFO PT101 contagens=130
2026-10-05 08:00:06 INFO PT102 contagens=1783
2026-10-05 08:00:06 INFO FT201 pulsos=3922
2026-10-05 08:00:06 INFO LT301 nivel=47.01
2026-10-05 08:00:12 INFO PT101 contagens=132
2026-10-05 08:00:12 INFO PT102 contagens=1795
2026-10-05 08:00:12 INFO FT201 pulsos=391
2026-10-05 08:00:12 INFO LT301 nivel=47.00
2026-10-05 08:00:18 INFO PT101 contagens=130
2026-10-05 08:00:18 INFO PT102 contagens=1789
2026-10-05 08:00:18 INFO FT201 pulsos=3875
2026-10-05 08:00:18 INFO LT301 nivel=46.98
2026-10-05 08:00:24 INFO PT101 contagens=131
2026-10-05 08:00:24 INFO PT102 contagens=1792
2026-10-05 08:00:24 INFO FT201 pulsos=3880
2026-10-05 08:00:24 INFO LT301 nivel=47.02
2026-10-05 08:00:30 INFO PT101 contagens=130
2026-10-05 08:00:30 INFO PT102 contagens=1787
2026-10-05 08:00:30 INFO FT201 pulsos=3878
2026-10-05 08:00:30 INFO LT301 nivel=46.99
2026-10-05 08:00:36 INFO PT101 contagens=131
2026-10-05 08:00:36 INFO PT102 contagens=1791
2026-10-05 08:00:36 INFO FT201 pulsos=3882
2026-10-05 08:00:36 INFO LT301 nivel=47.00
2026-10-05 08:00:42 INFO PT101 contagens=130
2026-10-05 08:00:42 INFO PT102 contagens=1788
2026-10-05 08:00:42 INFO FT201 pulsos=3879
"""

registros, _ = ler_log(log_texto)


class TestAcumuladorIngenuoExemplo(unittest.TestCase):
    """Exemplo do formato. `AcumuladorIngenuo` é código existente da base."""

    def test_sem_parcelas(self):
        """Sem nenhuma parcela, o total é zero."""
        self.assertEqual(AcumuladorIngenuo().total, 0.0)

# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #7 (escreva-os ANTES de corrigir o defeito e confirme que falham).

class TestAcumuladores(unittest.TestCase):
    """Testes de regressão da issue #7: acumuladores."""

    def test_acumulador_ingenuo(self):
        """AcumuladorIngenuo deve somar corretamente uma sequência de números."""
        acumulador = AcumuladorIngenuo()
        for x in range(1, 10):  # soma de 1 a 9
            acumulador.adicionar(x)
        self.assertAlmostEqual(acumulador.total, 45.0)  # 1+2+...+9 = 45

    def test_acumulador_kahan(self):
        """AcumuladorKahan deve somar corretamente uma sequência de números."""
        from elevatoria.acumuladores import AcumuladorKahan
        acumulador = AcumuladorKahan()
        n = 10000
        delta = 1e-5
        total_expected = n * delta
        for _ in range(0, n):  # soma de 1 a 9
            acumulador.adicionar(delta)
        self.assertAlmostEqual(acumulador.total, total_expected, places=14)  # 1000 * 0.01 = 10.0000000


class TestMedir(unittest.TestCase):
    """Exemplo do formato. `medir` é código existente da base (issue #6)."""

    def test_medicao_pt101(self):
        """Medição da tag PT101 com a curva do Marco 2."""
        curva = CurvaCalibracao([130, 131, 132, 133, 134], [1.0, 1.5, 2.0, 2.5, 3.0])
        medicao = medir(registros, "PT101", curva)
        self.assertAlmostEqual(medicao.medida.valor, 1.3125)

class TestAlturaManometrica(unittest.TestCase):
    """Exemplo do formato. `altura_manometrica` é código existente da base (issue #6)."""

    def test_altura_manometrica_ft201(self):
        """Altura manométrica da tag FT201 com a curva do Marco 2."""
        curva = CurvaCalibracao([130, 131, 132, 133, 134, 1795], [1.0, 1.5, 2.0, 2.5, 3.0, 833.5])
        altura = altura_manometrica(registros, curva)
        self.assertAlmostEqual(altura.valor, 84.7132593, places=6)  # valor aproximado esperado




if __name__ == "__main__":
    unittest.main()
