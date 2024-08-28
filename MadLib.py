#MadLib.py
#Name: Camdin Wagner McGuigan
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("car")
  name1 = input ("Aaron")
  noun2 = input ("supermarket")
  name2 = input ("Joe")
  verb1 = input ("slipped")
  verb2 = input ("dropping")
  #Print the story with the user supplied words.
  print("me and my friend" + name1 + "drove in a" + noun1 + "to the" + noun2 + "and saw our friend" + name2)
  print (name2 + verb1 + "and fell on his back after" + verb2 + "the millk")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
