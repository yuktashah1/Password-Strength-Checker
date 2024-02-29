#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def assess_password_strength(password):
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'\d', password))
    special_chars = bool(re.search(r'[^A-Za-z0-9]', password))

    criteria = {
        'length': length >= 8,
        'uppercase': uppercase,
        'lowercase': lowercase,
        'numbers': numbers,
        'special_chars': special_chars
    }
    strength = sum(criteria.values()) / len(criteria) * 100

    return strength, criteria

def display_strength_feedback(strength, criteria):
    print("Password Strength Assessment:")
    print("------------------------------")
    print(f"Length >= 8 characters: {'✓' if criteria['length'] else '✗'}")
    print(f"At least one uppercase letter: {'✓' if criteria['uppercase'] else '✗'}")
    print(f"At least one lowercase letter: {'✓' if criteria['lowercase'] else '✗'}")
    print(f"At least one number: {'✓' if criteria['numbers'] else '✗'}")
    print(f"At least one special character: {'✓' if criteria['special_chars'] else '✗'}")
    print(f"Overall Strength: {strength:.2f}%")

def provide_feedback(password, strength, criteria):
    print("Password Feedback:")
    print("------------------------------")
    if strength >= 80:
        print("Strong password! Keep it safe.")
    else:
        feedback = []
        if not criteria['uppercase']:
            feedback.append("Mixing uppercase and lowercase letters enhances security.")
        if not criteria['numbers']:
            feedback.append("Including numbers adds to the complexity of the password.")
        if not criteria['special_chars']:
            feedback.append("Special characters provide an extra layer of security.")
        print("Weak password. " + " ".join(feedback))

def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Please enter your password: ")
    strength, criteria = assess_password_strength(password)
    display_strength_feedback(strength, criteria)
    provide_feedback(password, strength, criteria)

if __name__ == "__main__":
    main()


# In[ ]:




