password = "Secure4648bv"

if len(password) < 6:
    strength = "weak"
elif len(password) <8:
    strength ="medium"
else:
    strength = "strong"
print("password strength is:", strength)

