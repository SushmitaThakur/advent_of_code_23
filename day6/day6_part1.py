import re

f = open("input.txt", "r")

times = []
distances = []

def getValues(line: str) -> list:

  result_list = line.split(":")
  matches = re.findall(r"\d+", result_list[1])
  values = [int(value) for value in matches]
  
  return values

for line in f:
  if re.search(r"Time", line):
    times = getValues(line)
    continue

  elif re.search(r"Distance", line):
    distances = getValues(line)

# print(times, distances)    

# Time:      7  15   30
# Distance:  9  40  200

races_won = [0] * len(times)

# for each race (time-distance pair)
for i in range(0, len(times)):

  race_time = times[i]
  race_distance = distances[i]
  # print(race_time, race_distance)

  for j in range(1, race_time):
    # if the button is pressed for 2 seconds, the speed will be 2 milimeters for the remaining time, 
    # if total race_time = 7 then
    # distance travelled = (7 - 2) * 2

    distance_travelled = (race_time - j) * j
    if distance_travelled > race_distance:
      races_won[i] = races_won[i] + 1

# Multiply all values 
result = 1
for value in races_won:
    result *= value

print(result)      