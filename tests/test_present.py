import pytest
from lib.present import *

def test_wrap():
    present = Present()
    present.wrap('toy')
    assert present.contents == 'toy'

def test_wrap_none():
    present = Present()
    present.wrap('toy')
    with pytest.raises(Exception) as error:
        present.wrap('game')
    error_message = str(error.value)
    assert error_message == 'A contents has already been wrapped.'

def test_unwrap():
    present = Present()
    present.wrap('toy')
    assert present.unwrap() == 'toy'

    