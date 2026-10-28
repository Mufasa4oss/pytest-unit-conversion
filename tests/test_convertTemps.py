from validator.convertTemps import convert
import pytest

def test_tempConversion():
    result = convert(0,"C","F")
    assert result == pytest.approx(32)
def test_type():
    result = convert(0,"C","F")
    result = type(result)
    assert result == float
def test_for_invalid_unit():
    with pytest.raises(ValueError):
        convert(27,"C","psi")