#list
from function2 import *
questions = ["", "", "", "", "", "", "", "", "", "", ""]
count = 0
def game(questions):
  a = input("Would you like to play?")
  if a == "yes":
    setup(a)
  elif a == "no":
    print("Your loss")