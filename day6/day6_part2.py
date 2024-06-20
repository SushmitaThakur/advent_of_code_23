import re

f = open("input.txt", "r")

def getValues(line: str) -> list:

  result_list = line.split(":")
  matches = re.search(r"\d+", result_list[1].replace(" ", ""))

  return int(matches[0])

for line in f:
  if re.search(r"Time", line):
    time = getValues(line)
    continue

  elif re.search(r"Distance", line):
    distance = getValues(line)

# print(time, distance)    

races_won = 0

for j in range(1, time):
  distance_travelled = (time - j) * j
  if distance_travelled > distance:
    races_won += 1

print(races_won)      