import re
import math

node_list = []
letters_list = []
file = open("input.txt", "r")
pattern = r"(?P<node>\w{3})\s=\s\((?P<left>\w{3}),\s(?P<right>\w+)\)"

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

def run_simulation(this_node: dict)-> int :
  i = 0
  steps = 0 
  
  while not this_node.endswith('Z'):
    letter =  letters_list[i]
    # print(letter)
    for node in node_list:
      if node["node"] == this_node:
        this_node = node[letter]
        break

    i += 1 
    steps += 1
    if i == len(letters_list):
      i = 0

  # print(steps)
  return steps

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# -----------------------------------------------
start_nodes = [node for node in node_list if node['node'].endswith('A')]
node_steps = []

for node in start_nodes:
  node_steps.append(run_simulation(node["node"]))

result = node_steps[0]
for num in node_steps[1:]:
    result = lcm(result, num)

print("\nSteps: ",result,)