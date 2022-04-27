#!/usr/bin/env python3

import requests


# Print instructions
def intro():

  print("-------------------------------------------------------------------------------------")
  print("**   **     **     ****  *******  ******  ******   **   **  *******  **    *  ****** ")
  print("* * * *    *  *   **        *     *       *     *  * * * *     *     * *   *  *     *")
  print("*  *  *   * ** *    **      *     ****    ******   *  *  *     *     *  *  *  *     *")
  print("*     *  *      *     **    *     *       *     *  *     *     *     *   * *  *     *")
  print("*     *  *      *  ****     *     ******  *     *  *     *  *******  *    **  ****** ")
  print("-------------------------------------------------------------------------------------\n")
  print("INSTRUCTIONS:\n")
  print("Try to guess the 4 digit combination.")
  print("The numbers are in the range 0-7.")
  print("You have 10 tries.")
  print("Good luck!\n")

  return


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
def mastermind(winning_nums):

  #print(winning_nums, "\n")
  print("Guess the combination. You have 10 tries.")

  i = 10
  possible_nums = ["0", "1", "2", "3", "4", "5", "6", "7"]

  while i > 0:
    guess_list = []
    guess = input("Choose any combination of 4 numbers from 0-7 --> ")

    for num in guess:
      if num not in possible_nums:
        print(f"{num} is an invalid guess. Choose 4 numbers between 0-7.")
        continue
      guess_list.append(num)
    
    print(guess_list)

    if len(guess_list) != 4:
      print("Must choose 4 numbers. Try again.")
      continue

    if guess_list == winning_nums:
      print("YOU WON YOU LUCKY SON OF A BITCH!")
      return

    # Functionality for exact and partially correct guesses here.
    else:
      exact = 0
      partial = 0
      winning_nums_copy = winning_nums.copy()
      guess_list_copy = guess_list.copy()

      # Check for exact matches
      for j in range(len(guess_list)):
        if guess_list[j] == winning_nums[j]:
          exact += 1
          winning_nums_copy.remove(guess_list[j])
          guess_list_copy.remove(guess_list[j])
        else:
          continue
      
      # Check for partial match      
      for k in range(len(guess_list_copy)):
        if guess_list_copy[k] in winning_nums_copy:
          partial += 1
          winning_nums_copy.remove(guess_list_copy[k])
        else:
          continue

      # Print formatting
      if exact == 1:
        y = "is"
      else:
        y = "are"

      if partial == 1:
        x = "number"
      else:
        x = "numbers"

      print(f"You got {partial + exact} {x} correct and {exact} {y} in the exact spot.")

      i -= 1
      print(f"Wrong. You have {i} tries left")

  print("You lost. Big time.")
  return


# Guess history and computer feedback function.
def get_history():

  history = "Hello!!!"

  return history


if __name__ == "__main__":

  intro()
  url = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
  winning_nums = get_random(url)
  mastermind(winning_nums)
