import re

RED_MAX = 12
BLUE_MAX = 14
GREEN_MAX = 13

pattern = r'(?: *(?P<red>\d+) red)?(?: *(?P<green>\d+) green)?(?: *(?P<blue>\d+) blue)?'
counter = 1
idTotal = 0

f = open("input.txt", "r")

for x in f:
  
  # Split the line by ':' and take the second part (assuming the numbers and colors are after the colon)
  matches = re.finditer(pattern, x.split(":", 1)[1])
  status = True

  for match in matches:
      named_groups = {name: int(value) for name, value in match.groupdict().items() if value is not None}
     
      if('blue' in named_groups and named_groups['blue'] > BLUE_MAX):
        status = False 
      if('red' in named_groups and named_groups['red'] > RED_MAX):
        status = False 
      if('green' in named_groups and named_groups['green'] > GREEN_MAX):
        status = False  

  if status == True:
    idTotal += counter

  counter += 1

print(idTotal)
f.close()