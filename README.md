# simplePasswordCheck
Very simple password check

- Checks password against length, character variety (uppercase, lowercase, digits, symbols).

- Detects common patterns and sequences (e.g., 1234, abcd, qwerty).

- Checks passwords against the 100k most commonly used passwords from Daniel Miessler’s SecLists.

- Provides a strength rating: Weak, Moderate, Strong, Very Strong.

- Gives feedback/suggestions for improving password security.

- Simple command-line interface (CLI) with an exit/quit option.

## ⚠️ Wordlist Requirement
This project uses the [100k-most-used-passwords-NCSC.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt) 
file from Daniel Miessler's SecLists repository.

# Before running the project:
- Please download this file and place it in the project folder before running:
- Place in project folder
- Run password checker with:
  - python password_checker.py 100k-most-used-passwords-NCSC.txt

## Future Improvements
- Entropy Calculation to measure true randomness for extra points to security score
- Visualize password strength with updating progress bar
- Fuzzy matching to catch slightly modified common passwords (Ex: 'Password' vs 'P@ssW0Rd')
