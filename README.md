# Password_Checker

## Overview
The **Password Checker** is a Python application designed to evaluate the security of a password. It performs several checks, including password length, character composition, common password usage, and assigns a security score with recommendations.

## Features
- **Length Validation**: Ensures the password meets a minimum length requirement.
- **Character Type Validation**: Checks for uppercase letters, lowercase letters, digits, and special characters.
- **Common Password Detection**: Identifies passwords that are commonly used and considered insecure.
- **Password Scoring**: Assigns a security level (Weak, Medium, Strong) based on the password’s characteristics.

## How It Works
1. **Password Input**: The user inputs a password.
2. **Validation Checks**: The application runs several checks to validate the password:
   - Length Check
   - Character Type Check
   - Common Password Check
3. **Security Scoring**: The password is scored based on its length, diversity of character types, and uniqueness.
4. **Feedback**: The application provides feedback and a security level for the password.

## Installation
### Requirements
- Python 3.6 or higher

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-checker
   ```
3. Run the application:
   ```bash
   python password_checker.py
   ```

## Usage
1. Run the script:
   ```bash
   python password_checker.py
   ```
2. Enter your password when prompted.
3. Receive feedback about the strength and security of your password.

## Example
```bash
Enter your password: MySecureP@ssword1
Your password is strong! Well done. (Security level: Strong)
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please contact:
- **GitHub**: [HasretIrmak](https://github.com/HasretIrmak)

