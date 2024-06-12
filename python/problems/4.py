print(sum((sum((len(persons[j][i]) for i in persons[j].keys())) for j in persons.keys())))
