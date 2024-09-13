# Personalized Wordlist Generator

## Overview

This Python script generates a personalized wordlist based on user input, such as personal information and special characters. It creates various combinations of the provided information, applies different letter cases, and adds special characters. The result is a comprehensive list of potential passwords, saved in a text file for later use.

## Features

- **Generate case variations**: For each string, the script generates all possible uppercase and lowercase combinations.
- **Add special characters**: Special characters can be appended or prepended to the strings.
- **Support for combinations and permutations**: The script combines multiple pieces of personal information in different ways to create a wide variety of wordlist entries.

## How It Works

The script asks the user for:
1. **Personal Information**: This is a comma-separated list (e.g., `John,Doe,1990`), which the script uses to generate wordlist entries.
2. **Special Characters**: The user can either provide their own special characters or use the default set (`!@#$%^&*()_+-=~\`[]{}|;:',.<>?/`).

It then generates:
- All possible combinations of the input strings.
- Variations of the input strings with special characters.
- Uppercase and lowercase variations of all strings.

The wordlist is saved as a `.txt` file named after the first piece of personal information.

## Installation

1. **Python**: Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Dependencies**: This script uses Python’s standard library. No external libraries are required.

## Usage

1. Clone or download the script.

2. Run the script using Python:

   ```bash
   python main.py
   ```

3. When prompted, enter the personal information (e.g., `John,Doe,1990`).

4. The script will ask if you want to edit the special characters. If you choose to modify them, enter your desired special characters. Otherwise, the script will use the default set.

5. The script generates a comprehensive wordlist and saves it to a file called `wordlist_<first_name>.txt`.

### Example Input:
```
Write the personal information (ex: John,Doe,1990...): John,Doe,1990
Edit special characters (default: !@#$%^&*()_+-=~`[]{}|;:',.<>?/) [Y/N]: N
```

### Example Output:
The wordlist will be saved as `wordlist_John.txt` and contain various combinations like:
```
john1990
Doe!
JOHNDOE!!
doE1990
johnDoe@#
...
```

## Customization

- You can customize the list of special characters by providing your own set when prompted.
- The wordlist generation logic can be expanded by modifying how permutations and combinations are handled in the script.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README explains the script's functionality, installation, and how to run it. Let me know if you want to make any changes or add more details!
