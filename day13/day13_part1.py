
def extract():
  file = open("input.txt")
  rocks = []
  for line in file:
    # Convert each character to a list
    character_list = [char for char in line if char != '\n']   

    rocks.append(character_list)

  return rocks  

def roll_the_rocks(rocks: list)-> list :


  for i in range(len(rocks[0])-1, -1, -1):

    for j in range(0, len(rocks[0])):
      if(i-1>=0):
        if(rocks[i][j] == 'O' and rocks[i-1][j] == '.' and rocks[i-1][j] != 'O'):
          rocks[i][j] = '.'
          rocks[i-1][j] = 'O'
   
      if i+1<len(rocks):  
        if(rocks[i][j] == '.'  and rocks[i+1][j] == 'O' ):
          rocks[i][j] = 'O'
          rocks[i+1][j] = '.'  

  return rocks

def calculate_sum(rolled_rocks: list)-> int:
  multiplier = len(rolled_rocks)
  total_sum = 0
  for row in rolled_rocks:
    O_counts = row.count("O")
    print("O-counts:", O_counts)
    total_sum += (O_counts * multiplier)
    multiplier -=1

  return total_sum

def main():
  rocks = extract()
  for k in range(0, len(rocks)):
    rolled_rocks = roll_the_rocks(rocks)
  for row in rolled_rocks:
    print(row,"\n")

  print("Total sum:", calculate_sum(rolled_rocks))
main()