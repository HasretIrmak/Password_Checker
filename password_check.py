import re

def check_password_length(password, min_length=8):
    """
    Checks the length of the password.
    :param password: User's password
    :param min_length: Minimum required length (default: 8)
    :return: Length validation result (bool) and message
    """
    if len(password) < min_length:
        return False, f"Password is too short! It should be at least {min_length} characters long."
    return True, "Password length is valid."

def check_password_characters(password):
    """
    Validates if the password contains required character types.
    :param password: User's password
    :return: Character validation result (bool) and message
    """
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character (e.g., !@#$%^&*)."
    return True, "Password character composition is valid."

def check_common_passwords(password):
    """
    Checks if the password is among commonly used passwords.
    :param password: User's password
    :return: Validation result (bool) and message
    """
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "qwerty", "abc123", "111111", "iloveyou",
        "password1", "admin", "welcome", "letmein"
    ]
    if password in common_passwords:
        return False, "This password is too common! Please choose a stronger password."
    return True, "Password is not commonly used."

def score_password(password):
    """
    Assigns a security score to the password.
    :param password: User's password
    :return: Security level and description
    """
    score = 0

    # Length scoring
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character type scoring
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Common password check
    is_common, _ = check_common_passwords(password)
    if not is_common:
        score += 1

    # Determine security level
    if score <= 3:
        return "Weak", "Your password is very weak! Consider creating a stronger password."
    elif score <= 5:
        return "Medium", "Your password is medium strength. You can make it stronger."
    else:
        return "Strong", "Your password is strong! Well done."

def password_checker(password):
    """
    Validates the password for length, character types, common usage, and security score.
    :param password: User's password
    :return: Security check messages
    """
    is_valid, message = check_password_length(password)
    if not is_valid:
        return message

    is_valid, message = check_password_characters(password)
    if not is_valid:
        return message

    is_valid, message = check_common_passwords(password)
    if not is_valid:
        return message

    level, message = score_password(password)
    return f"{message} (Security level: {level})"

if __name__ == "__main__":
    password = input("Enter your password: ")
    result = password_checker(password)
    print(result)
