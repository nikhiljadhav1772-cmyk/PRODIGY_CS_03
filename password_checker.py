import re

def check_password(password):
    score = 0
    feedback = []
    passed = []

    # 1. Length checks
    length = len(password)
    if length < 6:
        feedback.append("Too short — use at least 8 characters.")
    elif length < 8:
        feedback.append("Increase length to at least 8 characters.")
        score += 1
    elif length < 12:
        passed.append(f"Good length ({length} characters).")
        score += 2
    else:
        passed.append(f"Excellent length ({length} characters).")
        score += 3

    # 2. Uppercase letters
    if re.search(r'[A-Z]', password):
        passed.append("Contains uppercase letters.")
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    # 3. Lowercase letters
    if re.search(r'[a-z]', password):
        passed.append("Contains lowercase letters.")
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    # 4. Digits
    if re.search(r'[0-9]', password):
        passed.append("Contains numbers.")
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # 5. Special characters
    if re.search(r'[!@#$%^&*(),.?\":{}|<>_\-\+=/\\]', password):
        passed.append("Contains special characters.")
        score += 2
    else:
        feedback.append("Add special characters (e.g. @, #, $, !).")

    # 6. No spaces
    if ' ' in password:
        feedback.append("Avoid spaces in passwords.")
        score -= 1

    # Determine strength label
    if score <= 2:
        strength = "WEAK"
        bar = "[##        ]"
    elif score <= 4:
        strength = "MODERATE"
        bar = "[#####     ]"
    elif score <= 6:
        strength = "STRONG"
        bar = "[########  ]"
    else:
        strength = "VERY STRONG"
        bar = "[##########]"

    return strength, bar, score, passed, feedback


def main():
    print("=" * 45)
    print("       PASSWORD COMPLEXITY CHECKER")
    print("=" * 45)

    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")

        if password.lower() == 'quit':
            print("Goodbye!")
            break

        if not password:
            print("Password cannot be empty.")
            continue

        strength, bar, score, passed, feedback = check_password(password)

        print("\n" + "-" * 45)
        print(f"  Password : {'*' * len(password)}  ({len(password)} chars)")
        print(f"  Strength : {strength}")
        print(f"  Score    : {score}/8  {bar}")
        print("-" * 45)

        if passed:
            print("\n  [✔] What's good:")
            for p in passed:
                print(f"      • {p}")

        if feedback:
            print("\n  [✘] What to improve:")
            for f in feedback:
                print(f"      • {f}")

        print("-" * 45)


if __name__ == "__main__":
    main()
