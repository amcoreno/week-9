from random import randint

# The task is this: the program will ask for the user's name and then it will say
# something like: “Well John, I've thought of a number between 1 and 100 and you
# have only eight tries to guess it. What number do you think it is?” On each try, the
# # player will say a number and the program can answer for different things.


# 1 If the number the user said is less than 1 or greater than 100, it will tell them that  he/she has chosen a number that is out of play.
# 2 If the number the user chose is less than the number the program thought of, it will tell them that the answer is wrong, and that he/she chose a lower number than the secret number.
# 3 If the user chose a number greater than the secret number, it will let them know that it was greater.
# 4 And if the user got the secret number right, they will be informed that they have won,and how many tries that has taken them.
# 5 If the user has not guessed correctly in their first attempt, they will be asked again to choose another number and so on until they win or until their eight attempts are done.


playerName = input("What is your name?")
print(f"Well, {playerName}, I'm thinking of a number between 1 - 100. Try to guess it in under 8 tries.")
number = input("What number do you think it is?")

randomNumber = randint(1, 101)

for i in range(8):
  if int(number) == randomNumber:
    print(f"You guessed it right in {i + 1} tries")
  elif int(number) > 100:
    print("It's out of range.")
    number = input("What number do you think it is?")
  elif int(number) < 1:
    print("It's out of range.")
    number = input("What number do you think it is?")
  elif int(number) > randomNumber:
    print("The number you guessed it more than the number I picked!") 
    number = input("What number do you think it is?")
  elif int(number) <  randomNumber:
    print("The number you guessed is lesser than the number I picked!")
    number = input("What number do you think it is?")
  else:
      print("You didnt get it")