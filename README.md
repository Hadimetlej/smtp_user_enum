# Username Enumeration Script

This script is used for username enumeration as part of a penetration testing methodology. It attempts to check the validity of various usernames on a target system and logs the results. The output includes successful attempts and error messages from unsuccessful ones. 

## Features:
- Enumerates common system usernames to check for validity.
- Provides feedback on valid and invalid usernames.
- Useful for security audits and penetration testing scenarios.

## Requirements:
- Python 3.x (or any system with basic scripting capabilities).
- Network access to the target system (used for penetration testing purposes).

## Usage:
1. Clone the repository:
   ```bash
   git clone https://github.com/Hadimetlej/smtp_user_enum.git
   python3 -m venv smtp_user_enum-env
   source smtp_user_enum-env/bin/activate
   cd smtp_user_enum
   
   
