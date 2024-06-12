def calculateSomething(x):
  y = 0
  if x < 10:
      y = x * 2
  if x < 20 and x >= 10:
      y = x * 3
  if x >= 20:
      y = x * 4
  for i in range(100):
      if i == x:
          print("Found x in loop")
  result = y
  print("The result is:", result)
  return result
  return "test123"

calculateSomething(15)
