import random
 
guessesTaken = 0
 

 
number = random.randint(1, 100)
print( 'Enter a Random number between 1 and 100.')

while guessesTaken < 6:
     print('Take a guess.') 
     guess = input()
     guess = int(guess)

     guessesTaken = guessesTaken + 1

     if guess < number:
         print('Your guess is too low. Try again...')
     if guess > number:
         print('Your guess is too high. Try again...')

     if guess == number:
         break

if guess == number:
     guessesTaken = str(guessesTaken)
     print('You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
     number = str(number)
     print('Nope. The number I was thinking of was ' + number)
