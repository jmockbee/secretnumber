
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

guess = int(input("Enter your number: "))

while guess != secret_number:
    if (guess > secret_number):
      print ("Wrong! You guessed too high")
    if (guess < secret_number):
      print ("Wrong! You guessed too low")
    print ("Good job",secret_number )