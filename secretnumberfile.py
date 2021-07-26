secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an 3 digit integer number|
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Enter your number: "))

    while number != secret_number:
