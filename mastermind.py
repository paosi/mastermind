#!/usr/bin/env python3

import requests


# Fetches 4 random integers and returns them as a list.
def get_random(url):

  response = requests.get(url).text
  random_nums = []

  for i in response:
    if i == "\n":
      continue 
    random_nums.append(i)

  return random_nums


# Asks the user for a 4 number guess and compares it to the random numbers.
def guess_nums(winning_nums):

  print(winning_nums)
  print("Guess the combination. You have 10 tries.")

  i = 10

  while i > 0:
    guess_list = []
    guess = input("Choose any combination of 4 numbers from 0-7 --> ")

    for num in guess:
      guess_list.append(num)
    
    print(guess_list)

    if guess_list == winning_nums:
      print("YOU WON YOU LUCKY SON OF A BITCH!")
      return

    # Add functionality for partially correct guesses here.

    else:
      i -= 1
      print("Wrong. You have {x} tries left".format(x = i))

  print("You lost. Big time.")


# Guess history and computer feedback function.
def get_history():

  history = "Hello!!!"

  return history

if __name__ == "__main__":

  url = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
  winning_nums = get_random(url)
  guess_nums(winning_nums)
