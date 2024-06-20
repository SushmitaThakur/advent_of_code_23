import re
import json

file = open("input.txt", "r")

def find_the_hand_type(cards: str) -> int:

  # print(cards)
  # exclude 'J's from normal counting
  checked_chars = ['J']
  counts = []
  for i in range(0, len(cards)):

    if cards[i] not in checked_chars:
     
      current_count = cards.count(cards[i])
      counts.append(current_count)
      checked_chars.append(cards[i])
      # print(f'letter: {cards[i]}, counts: {current_count}')
  
  if len(counts) == 0:
    counts.append(5)
  else:
    j_counts = cards.count('J')
    if j_counts != 0:
      print(cards, counts) 
      max_value = max(counts)
      max_index = counts.index(max_value)
      counts[max_index] += j_counts
      print("New count: ", counts)

  # print (counts)
  if 5 in counts: 
    # print("Five of a kind")
    hand_type = 7

  elif 4 in counts:
    # print("Four of a kind")
    hand_type = 6

  elif 3 in counts and 2 in counts:
    # print ("Full house")
    hand_type = 5

  elif 3 in counts:
    # print ("Three of a kind")
    hand_type = 4

  elif counts.count(2) == 2:       
    # print ("Two pair")
    hand_type = 3

  elif counts.count(1) == 3:
    # print ("One pair")
    hand_type = 2

  else:
    # print ("High cards")     
    hand_type = 1

  return hand_type   

def map_it(hands: dict):

  # mapping
  letter_mapping = {
      'A': 'Z',
      'K': 'Y',
      'Q': 'X',
      # 'J': 'W',
      'T': 'V',
      '9': 'U',
      '8': 'S',
      '7': 'R',
      '6': 'P',
      '5': 'O',
      '4': 'N',
      '3': 'M',
      '2': 'L',
      'J': 'I'
  }

  for hand in hands:
    hand["oldcards"] = hand["cards"]
    for i in range(0, len(hand["cards"])):  
      if hand["cards"][i] in ['A','K','Q','J','T','9','8','7','6','5','4','3','2']:
        replace_with = letter_mapping.get(hand["cards"][i])
        # print(hand["cards"], replace_with)
        hand["cards"] = hand["cards"].replace(hand["cards"][i], replace_with)
  
  return hands

def rank_it(hands: dict)-> (dict, int): 
  highest_rank = len(hands)
  sum = 0

  for i in range(0, len(hands)):
    hands[i]["rank"] = highest_rank
    hands[i]["product"] = hands[i]["rank"] * hands[i]["bid"]
    sum +=  hands[i]["product"] 
    highest_rank -= 1
  
  return hands, sum   
 
hands = []
for line in file:

  line_values = line.split(" ")
 
  hand_type = find_the_hand_type(line_values[0])
  
  new_hand = { "cards": line_values[0], "bid": int(line_values[1]), "type": hand_type}
  hands.append(new_hand)

# Map the characters of 'cards' so that they are sortable
mapped_hands = map_it(hands)

# Arrange the dictionary based on values in descending order
sorted_hands = sorted(mapped_hands, key=lambda x: (x['type'], x['cards']), reverse=True)

# rank the hands, find product and final sum of the bid
ranked_hands, sum = rank_it(sorted_hands)

print(sum)

file.close()