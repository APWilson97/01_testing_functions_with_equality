class PasswordChecker:
    def check(self, password):
        if len(password) >= 8:
            for char in ['@', '$', '&']:
                if char in password:
                    return True
            raise Exception("Invalid password, must include at least 1 special character")
        else:
            raise Exception("Invalid password, must be 8+ characters.")