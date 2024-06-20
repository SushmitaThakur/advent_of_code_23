import re 

f = open("input.txt", "r")
totalScore = 0

def processCard(card):

  # split winning number and my numbers in the card
  split_result = card.split("|")
  # get card numbers as list elements from winning numbers 
  list1 = split_result[0].split(" ")
  # get card numbers as list elements for my numbers and also remove the trailing "\n" from last number of the list 
  list2 = [item.strip() for item in split_result[1].split(" ")]

   # Find common elements between the teo lists
  intersection_result = [item for item in list1 if item in list2]
  # remove empty values from the list
  filtered = list(filter(None, intersection_result))

  return len(filtered)

for x in f:
  
  cardMatches = processCard(x)

  cardScore = 0
  if (cardMatches > 0): 

    cardScore = 1
    # raise 2 to the power of length-1
    cardScore = 2**(cardMatches - 1)
 
  # print("cardScore = ", cardScore)
 
  totalScore += cardScore

print(totalScore)  
f.close()