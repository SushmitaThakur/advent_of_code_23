import re

def word_to_number(word):
  number_mapping = {
      'zero': 0,
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 9,
  }

  # Convert the word to lowercase for case-insensitivity
  lower_word = word.lower()

  number = number_mapping.get(lower_word)

  return number

f = open("input.txt", "r")
total = 0

for x in f:
  
  # Challenge 1 regex: matches = re.findall(r'\d', x)
  # Challenge 2
  matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", x)

  if(not matches[0].isdigit()):
    matches[0] = word_to_number(matches[0])
  
  if(not matches[-1].isdigit()):
    matches[-1] = word_to_number(matches[-1])   

  if(len(matches) == 1):
    matches.append(matches[0])
    
  thisNumber = int(str(matches[0]) + str(matches[-1]))

  total += thisNumber

print(total)

f.close()  