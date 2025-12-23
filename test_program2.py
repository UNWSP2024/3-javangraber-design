import program_2

def test_categorize_age_infant():
    assert 'infant' == program_2.categorize_age(1)

def test_categorize_age_child():
    assert 'child' == program_2.categorize_age(12)

def test_categorize_age_teenage():
    assert 'teenager' == program_2.categorize_age(13)

def test_categorize_age_adult():
    assert 'adult'== program_2.categorize_age(20)