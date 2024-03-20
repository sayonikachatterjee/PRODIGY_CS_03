def check_password_complexity(password):
    # Minimum length check
    if len(password) < 8:
        return False, "Password should be at least 8 characters long."
    
    # Uppercase check
    if not any(char.isupper() for char in password):
        return False, "Password should contain at least one uppercase letter."
    
    # Lowercase check
    if not any(char.islower() for char in password):
        return False, "Password should contain at least one lowercase letter."
    
    # Digit check
    if not any(char.isdigit() for char in password):
        return False, "Password should contain at least one digit."
    
    # Special character check
    special_chars = "!@#$%^&*()-_=+`~[{]}\\|;:'\",<.>/?"
    if not any(char in special_chars for char in password):
        return False, "Password should contain at least one special character."
    
    return True, "Password is complex and secured."

# Test the function
password = input("Enter your password: ")
is_complex, msg = check_password_complexity(password)
print(msg)