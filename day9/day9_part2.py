file = open("input.txt", "r")

list = []
for line in file:
  matches = [int(value) for value in line.split(" ")]
  list.append(matches)
file.close()

def get_sub_level(row: list) -> list:
  sub_level = []  
  for i in range(1, len(row)):
    sub_level.append(row[i] - row[i-1])
  return sub_level

extrapolated_value = 0

for row in list:
  row.reverse()
  all_zeros = False
  # sub = row[0]

  while not all_zeros:
   
    level_list = get_sub_level(row)
    extrapolated_value += row[-1] 
    row = level_list
    # sub = level_list[0] - sub
    all_zeros = all(value == 0 for value in level_list)
  # print(sub)
  # extrapolated_value += sub 
print("extraval: ", extrapolated_value)