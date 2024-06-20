import re

def extract():
  with open("input.txt", 'r') as file:
    # Read the content of the file
    file_content = file.read()

  sequence = file_content.split(",")
  return sequence

def get_hash_value(word):
  current_value = 0
  for i in range(0, len(word)):
    ascii = ord(word[i])
    current_value += ascii
    current_value *= 17
    current_value = current_value % 256
  return current_value

def calculate_sequence(seq:list)-> int :
  boxes = [{} for i in range(0, 256)]

  for word in seq:  
    matches = re.search(r'(\w+)(=|-)(\d+)?',word)
    current_value = get_hash_value(matches[1])
    print(word, current_value)
      # if the sign is '-'
    if(matches[2] == '-'):
      result = boxes[current_value].pop(matches[1],None)
      # print("popped:", result)

    # if the is "="
    elif(matches[2] == '='):
      boxes[current_value][matches[1]] = matches[3]

  return boxes

def focusing_power(boxes):
  # print(boxes)
  total_value = 0 
  box_num = 0
  for box in boxes:
    if len(box) != 0:
      print (box)
      item_num = 0
      for item in box:
        print ("box num:",box_num ,"item no:", item_num, box[item])
        total_value += (box_num + 1) * (item_num + 1) * int(box[item])
        item_num += 1
    box_num += 1  
  return total_value


# ---------------------------------------------------------------------------------------- #
sequence = extract()  
boxes = calculate_sequence(sequence)
result = focusing_power(boxes)
print(result)