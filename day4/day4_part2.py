import re 

f = open("input.txt", "r")

# no of cards in the input file
TOTAL_CARDS = 213

scratchcards = [1] * TOTAL_CARDS
cardCounter = 0

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

  # run the loop for all the instance of the current scratchcard
  for j in range(0, scratchcards[cardCounter]):
    for i in range(1, cardMatches+1):
      scratchcards[cardCounter+i] += 1

  cardCounter += 1

print(sum(scratchcards)) 
f.close()
