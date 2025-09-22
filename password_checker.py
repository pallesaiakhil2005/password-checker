import re
import random

def check_password(password):
    strength = 0
    tips = []

    # Check each rule
    if len(password) >= 8:
        strength += 1
    else:
        tips.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        tips.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        tips.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        tips.append("Add a number.")

    if re.search(r"[@$!%*?&#]", password):
        strength += 1
    else:
        tips.append("Add a special character (@, #, $, etc.).")

    # Strength level
    if strength == 5:
        level = "Strong 💪"
    elif strength >= 3:
        level = "Medium ⚡"
    else:
        level = "Weak ❌"

    return level, tips

def suggest_password(password):
    new_pass = password

    if len(new_pass) < 8:
        new_pass += str(random.randint(10, 99))
    if not re.search(r"[A-Z]", new_pass):
        new_pass = new_pass.capitalize()
    if not re.search(r"[0-9]", new_pass):
        new_pass += "123"
    if not re.search(r"[@$!%*?&#]", new_pass):
        new_pass += "@#"

    return new_pass

# --- Main Program ---
print("🔐 Simple Password Checker 🔐")
pwd = input("Enter password: ")

level, tips = check_password(pwd)
print("\nStrength:", level)

if tips:
    print("Suggestions:")
    for t in tips:
        print(" -", t)

print("\nExample stronger password:")
print("👉", suggest_password(pwd))