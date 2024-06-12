total = 0
for personID in persons.keys():
  for items in persons[personID].keys():
	  total += len(persons[personID][items])
print(total)
