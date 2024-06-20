import re

pattern = r'(?: *(?P<red>\d+) red)?(?: *(?P<green>\d+) green)?(?: *(?P<blue>\d+) blue)?'
counter = 1
gameTotal = 0

f = open("input.txt", "r")

for x in f:
  RED_MAX = 0
  BLUE_MAX = 0
  GREEN_MAX = 0

  # Split the line by ':' and take the second part (assuming the numbers and colors are after the colon)
  matches = re.finditer(pattern, x.split(":", 1)[1])
  status = True

  for match in matches:
      named_groups = {name: int(value) for name, value in match.groupdict().items() if value is not None}
     
      if('blue' in named_groups and named_groups['blue'] > BLUE_MAX):
        BLUE_MAX = named_groups['blue'] 

      if('red' in named_groups and named_groups['red'] > RED_MAX):
        RED_MAX = named_groups['red'] 

      if('green' in named_groups and named_groups['green'] > GREEN_MAX):
        GREEN_MAX = named_groups['green']  

  print(BLUE_MAX, RED_MAX, GREEN_MAX)

  gameTotal += (BLUE_MAX * RED_MAX * GREEN_MAX)

print(gameTotal)
f.close()