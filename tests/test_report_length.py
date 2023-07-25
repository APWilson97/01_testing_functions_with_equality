from lib.report_length import *

def test_ten_character_string():
    result = report_length('shdjekalmn')
    assert result == 'This string was 10 characters long.'

def test_five_character_string():
    result = report_length('maker')
    assert result == 'This string was 5 characters long.'

def test_string_with_symbols():
    result = report_length('hello!')
    assert result == 'This string was 6 characters long.'

def test_string_with_space():
    result = report_length('Hello World!')
    assert result == 'This string was 12 characters long.'

def test_string_with_emoji():
    result = report_length('Hey Denise😆')
    assert result == 'This string was 11 characters long.'

def test_string_with_int():
    result = report_length('356 sheeps')
    assert result == 'This string was 10 characters long.'