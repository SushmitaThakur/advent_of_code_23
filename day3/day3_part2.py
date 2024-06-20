class PartNumber:

  def __init__(self, start: int, end: int, number:int):
    self.start = start
    self.end = end
    self.number = int(number) 

  def is_adjacent(self, position: int) -> bool:
    return self.__in_range(position - 1) or self.__in_range(position) or self.__in_range(position + 1)

  def __in_range(self, position: int) -> bool:
    return self.start <= position <= self.end

class Symbol:

  def __init__(self, position: int, symbol: str):
    self.position = position
    self.symbol = symbol 
    self.adj_numbers = []


  def add_number(self, number: PartNumber) -> None:
    self.adj_numbers.append(number)

  # return the sum of all the numbers adjacent to this symbol
  def value(self):
    if self.is_gear():
      return self.adj_numbers[0].number * self.adj_numbers[1].number
    
    return sum([val.number for val in self.adj_numbers]) 

  def is_gear(self) -> bool:
    return self.symbol == '*' and len(self.adj_numbers) == 2 

file = open("input.txt")
number_list = []
symbol_list = []
for line in file:

  # for edge case when a digit is at the end of the line
  line += "."  
  number = ''
  num_row_list = []
  sym_row_list = []
  pos = -1

  start_pos = None

  for char in line:
    pos += 1
    if char == '\n':
      continue

    if char.isdigit():
      start_pos = pos if len(number) == 0 else start_pos
      # OR
      # start_pos = start_pos if start_pos is not None else pos 

      number += char
      continue
   
    if len(number) > 0:
      # position is pos-1 because we come here in the next round of finding a digit
      num_row_list.append(PartNumber(start_pos, pos - 1, number))
      number = ''

    if char != ".":
      sym_row_list.append(Symbol(pos,char))
    
  number_list.append(num_row_list)  
  symbol_list.append(sym_row_list)      
file.close()

current_row = total = 0
number_of_rows = len(symbol_list)

for sym_row in symbol_list:
  for sym in sym_row:

    num_to_check = []
    num_to_check += number_list[current_row]

    if current_row > 0:
      num_to_check += number_list[current_row - 1] 
    if current_row < (number_of_rows - 1):
      num_to_check += number_list[current_row + 1] 


    # print(current_row,sym.symbol)
    # print([num.number for num in num_to_check])
    
    for part_number in num_to_check:
      # print(part_number.is_adjacent(sym.position), sym.symbol)
      if part_number.is_adjacent(sym.position):
        sym.add_number(part_number)
    
    # print(sym.value())
    if sym.is_gear():
      total += sym.value()       

  current_row += 1 

print(total)
