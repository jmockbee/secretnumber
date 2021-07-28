
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an 3 digit integer number|
| to guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


secret_number = 777
guess = int(input("Enter your 3 digit number: "))
while guess != secret_number:

    if guess > secret_number:
       guess = int(input("Enter a number or  secret number to stop: "))
    elif guess < secret_number:
       guess = int(input("Enter a number or  secret number to stop: "))  
    else: 
        print ("Good job",secret_number )