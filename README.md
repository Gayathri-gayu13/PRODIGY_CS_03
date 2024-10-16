## Password Complexity Checker ##

This project is a comprehensive password strength assessment tool written in Python. It helps users ensure that their passwords meet security best practices by evaluating multiple aspects of the password's complexity. The tool provides real-time feedback to the user, helping them understand which areas of their password can be improved to enhance security.

#### Key Features:
- **Length Validation**: 
  - The tool rewards passwords that meet or exceed a minimum length of 8 characters, with extra points given for longer passwords (12+ characters).
  
- **Uppercase & Lowercase Letters**:
  - Strong passwords contain both uppercase and lowercase characters to increase complexity.
  
- **Numerical Characters**:
  - The tool checks if the password contains digits (0-9), which are crucial for adding complexity to the password.

- **Special Characters**:
  - The presence of special symbols (e.g., `!@#$%^&*()`) is checked to ensure that the password is harder to crack through brute force attacks.

- **Common Password Check**:
  - The tool compares the user’s password against a list of commonly used and weak passwords, flagging those that are highly guessable.

- **Pattern Detection**:
  - A penalty is applied if the password includes repetitive characters or sequences like "aaa" or "123", which can reduce the effectiveness of the password.

- **Granular Scoring System**:
  - Passwords are scored on a scale from 0 to 5 based on the number of criteria they meet. This allows for a more nuanced feedback system, which ranks passwords as "Weak", "Moderate", "Strong", or "Very Strong".

- **Detailed User Feedback**:
  - In addition to an overall score, the tool provides detailed suggestions for improving weak passwords, such as adding more variety in characters or increasing the length.


This tool is designed to educate users on password best practices and provide them with actionable feedback to make their accounts more secure!
