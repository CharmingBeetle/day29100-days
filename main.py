

def colourPicker (colour, word):
  if colour == "red":
    print("\033[31m", word, end="")
  elif colour == "blue":
    print("\033[34m", word, end="")
  elif colour == "green":
    print("\033[32m", word, end="")
  elif colour == "yellow":
    print("\033[33m", word, end="")
  elif colour == "purple":
    print("\033[35m", word, end="")
  elif colour == "pink":
    print("\033[1;31m", word, end="")
  elif colour == "orange":
    print("\033[1;33m", word, end="")
    
  else:
    print("\033[0m", word, end="")
    
print("Super Subroutine")
print()
print("With my", end="")
colourPicker("red", "new program")
colourPicker("reset", "I can just call purple('and')")
colourPicker("purple", "it will print in purple")
colourPicker("orange", "that word will appear in the color I set it to.")
colourPicker("blue", "Even blue. ")
colourPicker("reset", "With no")
colourPicker("green", "weird gaps.")
print()
colourPicker("pink", "Epic.")

