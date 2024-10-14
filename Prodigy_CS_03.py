import re

# Example of a common password list (for illustration, use a larger list in real implementation)
common_passwords = ["123456", "password", "123456789", "qwerty", "abc123"]

def assess_password_strength(password):
    score = 0
    feedback = []
    
    if password in common_passwords:
        feedback.append("Password is too common and easily guessable.")
        return "Very Weak password! (It's a common password)"

    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")
    
    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    if re.search(r"(.)\1\1", password):
        score -= 1
        feedback.append("Password contains too many repeated characters or sequences.")
    
    if score >= 5:
        return "Very Strong password!", feedback
    elif score == 4:
        return "Strong password!", feedback
    elif score == 3:
        return "Moderate password.", feedback
    else:
        return "Weak password. Please improve it.", feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)
print(strength)
if feedback:
    print("Feedback:")
    for item in feedback:
        print("-", item)
