from src.logic.calculators.calculadora_costos_escala import CalculadoraCostosEscala


def test_avance_mayor_al_ancho_maximo_no_falla():
    """Avance 393 mm (> 325 de ancho máquina) es válido: el avance no se limita por el ancho."""
    r = CalculadoraCostosEscala()._calcular_s3(393, es_manga=False)
    assert 'error' not in r
    assert abs(r['s3'] - 395.6) < 0.01
