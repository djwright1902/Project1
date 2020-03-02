#The point of this program is to create a funtion that will automatically score a word used in scrabble
def score(word):
 #set the value for points by letters to be counted by the function
  pointOne = ("L","l","N","n","O","o","A","a","I","i","E","e","S","s","R","r","T","t","U","u")
  pointTwo = ("G","g","D","d")
  pointThree = ("B","b","C","c","M","m","P","p")
  pointFour = ("F","f","H","h","V","v","W","w","Y","y")
  pointEight = ("J","j","X","x")
  pointTen = ("Q","q","Z","z")
 #score the word in the function
  score = 0
  for k in word:
    if k in pointOne:
      score += 1
    elif k in pointTwo:
      score += 2
    elif k in pointThree:
      score += 3
    elif k in pointFour:
      score += 4
    elif k in pointEight:
      score += 8
    elif k in pointTen:
      score += 10
    else:
      score += 0
  return (score)
#ask the user to start the program
choice = input("Would you like to score words in scrabble, y for yes and n for no")
#use a while loop in case user wants to check multiple words
while (choice == "y"):
  #ask the user for their word
  word = input("What is your word")
  #run the function, score the users word, and return the score back to the user
  print ("Your word scored %f in scrabble"%(score(word)))
  #ask the user if they would like to continue checking words score
  choice = input("do you want to continue checking scores of words, y for yes and n for no")

