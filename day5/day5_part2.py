import re 

class Map:
  def __init__(self, destination: int, source: int, length: int ):
    self.destination = destination
    self.source = source
    self.length = length

  def in_range(self, number: int) -> bool: 
    return number in range(self.source, self.source+self.length+1)

  def get_mapping(self, number: int) -> int:
    distance = number - self.source
    return (self.destination + distance)
  
def extract_data():
  f = open("input.txt", "r")
  seeds = []
  thisFactor = ''
  numbers = {}

  for line in f:

    if line == "\n":
      continue

    if "seeds:" in line:
      seeds = re.findall(r"\d+", line)
      seeds = [int(value) for value in seeds]
      continue

    if ":" in line:
      thisFactor = (re.search(r"to-(?P<factor>\w+)", line)).groupdict()['factor']
      numbers[thisFactor] = []
    #  print(thisFactor)
      continue
    
    data = re.findall(r'\d+', line)
    data = [int(number) for number in data]

    numbers[thisFactor].append(Map(data[0], data[1], data[2]))
  
  f.close() 
  return seeds, numbers
  
def main():

  seeds, numbers = extract_data()
  # print(seeds, numbers)

  locations = []

  seeds = [seeds[i:i+2] for i in range(0,len(seeds), 2)] 

  # print (seeds)
  
  lowestLocation = float('inf')

  for seedPair in seeds:
    for i in range(seedPair[0], seedPair[0]+seedPair[1]):
      if i % 10000 == 0:
        print(i)

      result = i
      for factor, mappings in numbers.items(): # numbers ['soil' => [map1, map2, ...], 'fert' => [map1, map2, ...]]
        
        for map in mappings:
        
          if map.in_range(result):
            # print(map.destination, map.source, map.length)
            result = map.get_mapping(result)
            break
      
      if result < lowestLocation:
        lowestLocation = result

  print(lowestLocation)

main()