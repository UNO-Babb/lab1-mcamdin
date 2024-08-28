#MadLib.py
#Name: Camdin Wagner McGuigan
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("enter a noun: ")
  name1 = input ("enter a name: ")
  noun2 = input ("enter a noun: ")
  name2 = input ("enter a name: ")
  verb1 = input ("enter a verb: ")
  verb2 = input ("enter a verb: ")
  #Print the story with the user supplied words.
  print("me and my friend " + name1 + " drove in a " + noun1 + " to the " + noun2 + " and saw our friend " + name2)
  print (name2 + verb1 + " and fell on his back after " + verb2 + " the millk ")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
