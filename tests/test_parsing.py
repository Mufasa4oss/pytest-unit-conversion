from validator.parsing import parse_reading

def test_parsing():
    result = parse_reading("id:0192,92,F")
    assert result == ("id:0192",92,"F")