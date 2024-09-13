import itertools

def generate_all_cases(s):
    cases = []
    for c in itertools.product(*((char.lower(), char.upper()) for char in s)):
        cases.append(''.join(c))
    return cases

def add_special_characters(s, special_chars):
    all_cases = set()

    # Default: 2
    for chars in itertools.product(special_chars, repeat=2):
        special_string = ''.join(chars)
        all_cases.update(generate_all_cases(special_string + s))
        all_cases.update(generate_all_cases(s + special_string))
    
    all_cases.update(generate_all_cases(s))

    return list(all_cases)

def generate_all_combinations(strings, special_chars):
    all_cases = set()

    for s in strings:
        all_cases.update(add_special_characters(s, special_chars))

    for r in range(2, len(strings) + 1):
        for combination in itertools.permutations(strings, r):
            combined = ''.join(combination)
            all_cases.update(add_special_characters(combined, special_chars))
    
    for r in range(1, len(strings) + 1):
        for combination in itertools.combinations(strings, r):
            combined = ''.join(combination)
            all_cases.update(add_special_characters(combined, special_chars))
    
    return list(all_cases)

personal_info = input("Write the personal information (ex: John,Doe,1990...): ")

default_special_chars = "!@#$%^&*()_+-=~`[]{}|;:',.<>?/"

special_chars = input(f"Edit special characters (default: {default_special_chars}) [Y/N]: ")
if special_chars.lower() == "y":
    special_chars = input("Enter special characters: ")
else:
    special_chars = default_special_chars

passwords = generate_all_combinations(personal_info.split(","), special_chars)

with open(f"wordlist_{personal_info.split(',')[0]}.txt", "w") as f:
    for password in passwords:
        f.write(password + "\n")

print("Wordlist created successfully!")