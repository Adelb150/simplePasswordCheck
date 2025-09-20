import re
import sys
import os


# Load common passwords into a set
def load_common_passwords(filepath: str) -> set[str]:
    if not os.path.exists(filepath):
        print(f"[!] Could not find password list at: {filepath}")
        sys.exit(1)

    common = set()
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pw = line.strip()
            if pw:
                common.add(pw.lower())
    return common


# Password strength evaluation
def password_strength(password: str, common_passwords: set[str]) -> tuple[str, list[str]]:
    feedback = []
    score = 0
    pw_lower = password.lower()

    # 1. Check if in common-password list
    if pw_lower in common_passwords:
        feedback.append("❌ This password is in the top 100k most-used passwords. Choose something unique!")
        return "Very Weak", feedback

    # 2. Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Use at least 12 characters.")

    # 3. Character variety checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("⚠️ Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("⚠️ Add a special character (e.g., !@#$%^&*).")

    # 4. Detect simple sequences (1234, abcd, qwerty, etc.)
    if re.search(r"(1234|abcd|qwerty|password)", pw_lower):
        feedback.append("⚠️ Avoid simple sequences or obvious words.")

    # 5. Final rating
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    elif score <= 6:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, feedback



# main loop

def main():
    if len(sys.argv) != 2:
        print("Usage: python password_checker.py <path-to-100k-password-file>")
        sys.exit(1)

    password_file = sys.argv[1]
    common_passwords = load_common_passwords(password_file)

    print("\n🔐 Password Strength Checker")
    print("Type 'exit' to quit.\n")

    while True:
        pw = input("Enter a password to check: ").strip()
        if pw.lower() == "exit":
            print("Goodbye!")
            break

        rating, feedback = password_strength(pw, common_passwords)
        print(f"\nPassword Strength: {rating}")

        if feedback:
            print("Suggestions:")
            for f in feedback:
                print(" -", f)
        print("-" * 40)


if __name__ == "__main__":
    main()
