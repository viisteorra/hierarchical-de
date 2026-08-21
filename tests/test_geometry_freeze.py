"""The geometric core cannot silently become a fit parameter."""

from pathlib import Path

from geometry import OMEGA_DE_TODAY, Q4_WEIGHT, Q5_WEIGHT, r

SRC = Path(__file__).resolve().parents[1] / "src" / "geometry.py"


def test_source_still_hardcodes_the_1_11_rule():
    text = SRC.read_text()
    assert "Q4_WEIGHT = 1" in text
    assert "Q5_WEIGHT = 11" in text
    assert "OMEGA_DE_TODAY = r / (1 - r)" in text
    assert "minimize" not in text
    assert "chi2" not in text.lower()


def test_exact_rational_tail():
    # 4.9/7.1 = 49/71. Floating 2/5 is exact in the IEEE value Python uses here.
    assert abs(OMEGA_DE_TODAY - 49 / 71) < 1e-12
    assert Q4_WEIGHT / Q5_WEIGHT == 1 / 11
    assert abs(r - 49 / 120) < 1e-12
