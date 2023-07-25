from lib.string_builder import * 

def test_add_hello():
    string_builder = StringBuilder()
    string_builder.add('hello')
    assert string_builder.str == 'hello'

def test_add_hello_length():
    string_builder = StringBuilder()
    string_builder.add('hello')
    assert string_builder.str == 'hello' 
    assert string_builder.size() == 5

def test_output_hello():
    string_builder = StringBuilder()
    string_builder.add('hello')
    assert string_builder.output() == 'hello'

def test_add_two_strings_with_space():
    string_builder = StringBuilder()
    string_builder.add('hello')
    string_builder.add(' world')
    assert string_builder.size() == 11
    assert string_builder.output() == 'hello world'

