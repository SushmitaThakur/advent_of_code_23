def extract():
  with open("input.txt", 'r') as file:
    # Read the content of the file
    file_content = file.read()

  sequence = file_content.split(",")
  return sequence

def calculate(seq:list)-> int :
  total_value = 0 
  for word in seq:
    current_value = 0
    for i in range(0, len(word)):
      ascii = ord(word[i])
      current_value += ascii
      current_value *= 17
      current_value = current_value % 256
    total_value += current_value
  return total_value
  
sequence = extract()  

result = calculate(sequence)
print(result)