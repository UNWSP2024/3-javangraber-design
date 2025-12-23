import program_3

# Using string conversions in case they elect to not add trailing 0's in their logic.
def test_11_weight():
    assert "52.25" in str(program_3.weight_conversion(11))

def test_7_weight():
    assert "28" in str(program_3.weight_conversion(7))

def test_3_weight():
    assert "9" in str(program_3.weight_conversion(3))

def test_1_weight():
    assert "1.5" in str(program_3.weight_conversion(1))