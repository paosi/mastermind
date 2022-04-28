#!/usr/bin/env python3

import requests
import os
from playsound import playsound


# Print instructions
def intro():

  sounds = os.path.join(os.getcwd(), "sounds", "")
  
  print("-------------------------------------------------------------------------------------")
  print("**   **     **     ****  *******  ******  ******   **   **  *******  **    *  ****** ")
  print("* * * *    *  *   **        *     *       *     *  * * * *     *     * *   *  *     *")
  print("*  *  *   * ** *    **      *     ****    ******   *  *  *     *     *  *  *  *     *")
  print("*     *  *      *     **    *     *       *     *  *     *     *     *   * *  *     *")
  print("*     *  *      *  ****     *     ******  *     *  *     *  *******  *    **  ****** ")
  print("-------------------------------------------------------------------------------------\n")
  print("                                   INSTRUCTIONS:\n")
  print("                     ------------------------------------------")
  print("                     |  Try to guess the 4 digit combination. |")
  print("                     |    The numbers are in the range 0-7.   |")
  print("                     |           You have 10 tries.           |")
  print("                     |               Good luck!               |")
  print("                     ------------------------------------------\n")
  playsound(sounds + "001.mp3")

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

  sounds = os.path.join(os.getcwd(), "sounds", "")

  #print(winning_nums, "\n")
  print("Guess the combination. You have 10 tries remaining.")
  print("---------------------------------------------------")
  playsound(sounds + "002.wav")

  i = 10
  possible_nums = ["0", "1", "2", "3", "4", "5", "6", "7"]
  ignore = ["-", ",", ".", "/", " "]

  while i > 0:

    guess_list = []

    # Get user input and remove whitespace, comma, period, etc., if any.
    guess = input("Choose any combination of 4 numbers from 0-7 --> ")
    playsound(sounds + "002.wav")
    guess_copy = guess
    for g in guess_copy:
      if g in ignore:
        guess =  guess.replace(g, "")

    # Make sure user inputs are valid numbers.
    for char in guess:
      if char not in possible_nums:
        print(f"{char} is an invalid guess. Choose 4 numbers between 0-7.")
        continue
      guess_list.append(char)

    # Make sure user chooses 4 valid numbers only.
    if len(guess_list) != 4:
      print("Must choose 4 numbers. Try again.")
      playsound(sounds + "004.mp3")
      continue

    print(guess_list)

    if guess_list == winning_nums:
      print("YOU ARE A WINNER!")
      playsound(sounds + "005.wav")
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
      if (partial + exact) > 0:
        playsound(sounds + "003.mp3")

      i -= 1
      print(f"Try again. You have {i} tries remaining.")
      print("---------------------------------------------------")

  print("You lost. Big time.")
  playsound(sounds + "006.wav")
  return



if __name__ == "__main__":

  url = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
  
  intro() 
  mastermind(get_random(url))
