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

# print(letters_list, node_list)

start_nodes = [node for node in node_list if node['node'].endswith('A')]
len_start_nodes = len(start_nodes)
len_letters_list = len(letters_list)
i = 0
steps = 0 

print("\nStep: ",steps,"Start Nodes:", start_nodes)
while 1:

  next_nodes = []
  direction =  letters_list[i]

  for node in start_nodes:
    next_nodes.append(node[direction])

  i += 1 
  steps += 1
  if i == len_letters_list:
    i = 0

  len_nodes_with_Z = len([value for value in next_nodes if value.endswith('Z')])

  if len_start_nodes == len_nodes_with_Z:
    goal_achiedved = True
    break

  start_nodes = [node for node in node_list if node['node'] in next_nodes]
  print("\nStep: ",steps,"Start Nodes:", start_nodes)

print("\n\nTotal Steps: ",steps,"final Nodes:", next_nodes)
