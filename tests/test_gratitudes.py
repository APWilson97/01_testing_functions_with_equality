from lib.gratitudes import *

def test_if_list_is_initially_empty():
    result = Gratitudes()
    assert result.gratitudes == []

def test_if_adds_strings_correctly():
    result = Gratitudes()
    result.add('Thank you')
    assert result.gratitudes == ['Thank you']

def test_if_formats_correctly():
    result = Gratitudes()
    result.add('Thank you')
    result.add('Cheers')
    assert result.format() == 'Be grateful for: Thank you, Cheers'

def test_if_spaces_are_handled():
    result = Gratitudes()
    result.add('Family')
    result.add(' Eoin')
    assert result.format() == 'Be grateful for: Family,  Eoin'

