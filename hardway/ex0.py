def sum_double(a, b):
  return (a + b) if a != b else 2 * (a + b)

print(sum_double(2, 2))


def front_back(str):
  if len(str) <= 1:
    return str
    
  return str[-1] + str[1:-1] + str[0]

print(front_back("abcde"))


def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  
  return result

print(string_bits("abcdef"))


def last2(str):
  if len(str)<=2:
      return 0
      
  sample = str[-2:]
  
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == sample and i < len(str)-2:
      count += 1
      
  return count

print(last2("xaxxaxaxx"))