import random

print("Welcome to the game \"guess the number\"")
play = True
while play:
  print("Enter maximum number")
  right_range = int(input())
  num = random.randint(1, right_range)
  cnt = 0

  def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= right_range:
      return True
    print(f"Or maybe we will enter a number from 1 to {right_range}?")
    return False

  while True:
    print(f"Enter a number from 1 to {right_range}")
    num2 = input()
    if is_valid(num2): 
      cnt+=1
      num2 = int(num2)
      if num2 == num:
        print("You guessed it, congratulations!\nNumber of tries: ", cnt)
        break
      elif num2 > num:
        print("Your number is higher than expected, please try again")
      else: 
        print("Your number is less than expected, please try again")
    else:
      print("Please enter valid input")

  print("Do you want to play again? (yes(y)/no(n))")
  ans = input().lower()
  if ans == "y": 
    play = True
  else: play = False

print("Thanks for playing the number guessing game. See you...")
