from lib.check_codeword import *

def test_if_codeword_is_horse():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_codeword_is_similar_to_horse():
    result = check_codeword('hase')
    assert result == 'Close, but nope.'

def test_codeword_is_not_horse():
    result = check_codeword('dog')
    assert result == 'WRONG!'