import pytest 
from lib.password_checker import *

def test_check_valid_password():
    password = PasswordChecker()
    assert password.check('skdjfbvh@') == True

def test_check_invalid_password():
    password = PasswordChecker()
    with pytest.raises(Exception) as error:
        password.check('hhh')
    error_message = str(error.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_check_without_special_char():
    password = PasswordChecker()
    with pytest.raises(Exception) as error:
        password.check('hdjsncmd')
    error_message = str(error.value)
    assert error_message == 'Invalid password, must include at least 1 special character'