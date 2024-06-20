import re

file = open("input.txt", "r")

pattern = r"(?P<node>\w{3})\s=\s\((?P<left>\w{3}),\s(?P<right>\w+)\)"
node_list = []
letters_list = []

for line in file:
  if len(letters_list) == 0:
    direction = re.findall(r"[RL]+", line)

    if len(direction) != 0:
      letters_list =  [letter for letter in direction[0]]

  else:  
    matches = re.findall(pattern, line) 
    for match in matches:
      if len(match) != 0:
        new_node = { "node": match[0], "L": match[1], "R": match[2]}
        node_list.append(new_node)
file.close()
# print(letters_list, node_list)

i = 0
steps = 0 
this_node = 'AAA'

while this_node != "ZZZ":

  letter =  letters_list[i]

  for node in node_list:
    # print(node)
    if node["node"] == this_node:
      this_node = node[letter]
      break

  i += 1 
  steps += 1
  if i == len(letters_list):
    i = 0

print(steps)