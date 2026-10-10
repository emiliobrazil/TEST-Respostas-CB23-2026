"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest
import numpy as np
from elevatoria.dados import contagem_por_tag, medir_tempos, por_tag
from elevatoria.dados import LINHA
from elevatoria.dados import valida_tag
from elevatoria.dados import ler_log
from elevatoria.dados import Registro
from elevatoria.dados import contagem_por_tag
from elevatoria.dados import serie
from elevatoria.dados import criar_conversores
from elevatoria.dados import medir_memoria
from elevatoria.dados import medir_tempos
from elevatoria.serie import SerieTemporal


# usado em TestContagemPorTag e TestSerie
registros = [
            Registro(instante=None, nivel="INFO", tag="PT101", valores={"contagens": 131.0}),
            Registro(instante=None, nivel="INFO", tag="PT101", valores={"contagens": 130.0}),
            Registro(instante=None, nivel="INFO", tag="PT102", valores={"contagens": 1790.0}),
            Registro(instante=None, nivel="INFO", tag="FT201", valores={"pulsos": 3873.0}),
            Registro(instante=None, nivel="INFO", tag="B1", valores={"evento": "partida"}),
        ]

class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])


class TestLINHA(unittest.TestCase):
    """Testes da regex LINHA (issue #1)."""

    def test_linha_valida(self):
        """Linha válida casa com a regex LINHA."""
        linha = "2026-10-05 08:00:00 INFO PT101 contagens=131"
        self.assertIsNotNone(LINHA.fullmatch(linha))

    def test_linha_invalida(self):
        """Linha inválida não casa com a regex LINHA."""
        linha = "2024-06-01 12:34:56 INVALID PT101 1234"
        self.assertIsNone(LINHA.fullmatch(linha))

class TestValidaTag(unittest.TestCase):
    """Testes da função valida_tag (issue #1)."""

    def test_tag_valida(self):
        """Tag válida é reconhecida."""
        tags_validas = ["PT101", "FT201", "B1", "A12", "Z99", "XY123"]
        for tag in tags_validas:
            with self.subTest(tag=tag):
                self.assertTrue(valida_tag(tag))

    def test_tag_invalida(self):
        """Tag inválida é rejeitada."""
        tags_invalidas = ["pt101", "PT", "PT1010", "101PT", "PT101 ", "PT101x"]
        for tag in tags_invalidas:
            with self.subTest(tag=tag):
                self.assertFalse(valida_tag(tag))

class TestLerLog(unittest.TestCase):
    """Testes da função ler_log (issue #1)."""

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
"""

    def test_ler_log_vazio(self):
        """Texto vazio devolve listas vazias."""
        registros, invalidas = ler_log("")
        self.assertEqual(registros, [])
        self.assertEqual(invalidas, [])

    def test_ler_log(self):
        """Linhas válidas são convertidas em Registro; linhas inválidas são listadas."""
        registros, invalidas = ler_log(self.log_texto + "\n2026-10-05 08:00:12 INVALID PT101 contagens=132")
        self.assertEqual(len(registros), 10)
        self.assertEqual(len(invalidas), 1)
        self.assertEqual(invalidas[0], "2026-10-05 08:00:12 INVALID PT101 contagens=132")
        self.assertEqual(registros[0].tag, "B1")
        self.assertEqual(registros[0].valores, {"evento": "partida", "corrente": 47.5})
        self.assertEqual(registros[1].tag, "PT101")
        self.assertEqual(registros[1].valores, {"contagens": 131.0})

class TestContagemPorTag(unittest.TestCase):
    """Testes da função contagem_por_tag (issue #1)."""

    def test_contagem_por_tag(self):
        """Contagem de registros por tag é correta."""

        resultado = contagem_por_tag(registros)
        esperado = {"PT101": 2, "PT102": 1, "FT201": 1, "B1": 1}
        self.assertEqual(resultado, esperado)

    def test_contagem_por_tag_vazio(self):
        """Lista vazia de registros devolve dicionário vazio."""
        resultado = contagem_por_tag([])
        self.assertEqual(resultado, {})

    def test_contagem_por_tag_unica(self):
        """Lista com registros de uma única tag devolve contagem correta."""
        registros = [
            Registro(instante=None, nivel="INFO", tag="PT101", valores={"contagens": 131.0}),
            Registro(instante=None, nivel="INFO", tag="PT101", valores={"contagens": 130.0}),
        ]
        resultado = contagem_por_tag(registros)
        esperado = {"PT101": 2}
        self.assertEqual(resultado, esperado)

class TestSerie(unittest.TestCase):
    """Testes da função serie (issue #1)."""

    def test_serie(self):
        """Criação de SerieTemporal a partir de registros filtrados por tag e chave."""
        resultado = serie(registros, "PT101", "contagens")
        esperado = [131.0, 130.0]
        self.assertTrue(np.allclose(resultado, esperado))

    def test_serie_sem_chave(self):
        """Registros da tag sem a chave são ignorados."""
        registros = [
            Registro(instante=None, nivel="INFO", tag="PT101", valores={"contagens": 131.0}),
            Registro(instante=None, nivel="INFO", tag="PT101", valores={}),  # sem contagens
            Registro(instante=None, nivel="INFO", tag="PT102", valores={"contagens": 1790.0}),
        ]
        resultado = serie(registros, "PT101", "contagens")
        esperado = [131.0]
        self.assertTrue(np.allclose(resultado, esperado))

class TestCriarConversores(unittest.TestCase):
    """Testes da função criar_conversores (issue #2)."""

    def test_criar_conversores(self):
        """Criação de conversores por tag é correta."""
        escalas = {"PT101": 2.0, "PT102": 3.0}
        conversores = criar_conversores(escalas)
        self.assertEqual(conversores["PT101"](5), 10.0)
        self.assertEqual(conversores["PT102"](5), 15.0)

class TestMedirMemoria(unittest.TestCase):
    """Testes da função medir_memoria (issue #3)."""

    def test_medir_memoria(self):
        """Medir memória de uma função simples."""
        arrayTeste = np.arange(1000, dtype=np.int32)
        memoria_usada = medir_memoria(arrayTeste)
        self.assertGreater(memoria_usada["float64"], 0)
        self.assertIn("list", memoria_usada)
        self.assertIn("array('H')", memoria_usada)
        self.assertIsInstance(memoria_usada["uint16"], int)
        self.assertIsInstance(memoria_usada["int32"], int)


class TestMedirTempos(unittest.TestCase):
    """Testes da função medir_tempos (issue #3).    
    """

    def test_medir_tempos(self):
        """Medir tempos de uma função simples."""
        arrayTeste = np.arange(1000, dtype=np.int32)
        tempos_usados = medir_tempos(arrayTeste, k=5)
        self.assertIn("laço", tempos_usados)
        self.assertIn("compreensão", tempos_usados)
        self.assertIn("map+lambda", tempos_usados)
        self.assertIn("vetorizado", tempos_usados)
        for chave in tempos_usados:
            self.assertIsInstance(tempos_usados[chave], float)
            self.assertGreaterEqual(tempos_usados[chave], 0.0)
        

class TestMediaMovel(unittest.TestCase):
    """Testes da função media_movel (issue #4)."""

    def test_media_movel(self):
        """Média móvel de uma série simples."""
        st = SerieTemporal.de_lista([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
        resultado = st.media_movel(janela=3)
        esperado = np.array([2.0, 3.0, 4.0, 5.0, 6.0])
        self.assertTrue(np.allclose(resultado, esperado))

class TestReamostrar(unittest.TestCase):
    """Testes da função reamostrar (issue #5)."""

    def test_reamostrar(self):
        """Reamostragem de uma série simples."""
        st = SerieTemporal.de_lista([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        resultado = st.reamostrar(k=2)
        esperado = np.array([1.5, 3.5, 5.5])
        self.assertTrue(np.allclose(resultado, esperado))

    def test_reamostrar(self):
        """Reamostragem de uma série simples com sobra."""
        st = SerieTemporal.de_lista([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
        resultado = st.reamostrar(k=2)
        esperado = np.array([1.5, 3.5, 5.5])
        self.assertTrue(np.allclose(resultado, esperado))

if __name__ == "__main__":
    unittest.main()

