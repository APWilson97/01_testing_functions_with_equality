from lib.greet import *

def test_if_name_is_alex():
    result = greet('Alex')
    assert result == 'Hello, Alex!'


