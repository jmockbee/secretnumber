
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an 3 digit integer number|
| and guess what number I've     |
| picked for you.                |
| So, what is the secret_number number? |
+================================+
""")


secret_number = 777


guess = int(input("Enter your number: "))



while guess != secret_number:
        print ("try your guess again .")

        guess = int(input("Take a guess.\n")

    else:
        
        print ("Good job:", secret_number )