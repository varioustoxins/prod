from .prod import prod


def test_basi_cprod():
    result = prod()
    
    assert result == 0

