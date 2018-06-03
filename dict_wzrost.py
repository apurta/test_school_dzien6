data = [{"height": 173, "first_name": "John", "last_name": "Doe"},
        {"height": 183, "first_name": "Anne", "last_name": "Nope"},
        {"height": 133, "first_name": "John", "last_name": "Nowak"},
        {"height": 173, "first_name": "Jack", "last_name": "Kowal"}]



for record in data:
    print (record["height"])

# wypisuje tylko wzrosty


total = 0
for record in data:
    total += record["height"]  #sumuje wszytskie wzrosty

print("Srednia: ", total/len(data))

#policzyliśmy średnią wzrostu wszystkich osób


heights_by_name = {}  # tworzymy słownik na imiona z odp im wzrostami

for record in data:
   if record["first_name"] in heights_by_name:
       heights_by_name[record["first_name"]].append(record["height"]) # jeśli takie imie jest już na liście to dopisujemy wzrost
   else:
       heights_by_name[record["first_name"]] = [record["height"]] # jeśli nie ma takiego imienia na liście tworzymy nową listę

print(heights_by_name)

#mamy nowy słownik

for name, heights in heights_by_name.items(): #iterujemy żeby dostać pary danych (bez .items chodziłby tylko po kluczach)
    print(name, sum(heights) / len(heights)) #wypisujemty imie i odpowiadającą im sume dziel przez wzorsty


print()
print()

#inny sposób

total_by_name = {}
count_by_name = {}

for record in data:
    first_name = record["first_name"]
    if first_name in total_by_name:
        total_by_name[first_name] += record["height"]
        count_by_name[first_name] += 1
    else:
        total_by_name[first_name] = record["height"]
        count_by_name[first_name] = 1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])

print()
print()
# z .get (jeszcze inny sposób)

total_by_name = {}
count_by_name = {}

for record in data:
    first_name = record["first_name"]
    total_by_name[first_name] = total_by_name.get(first_name, 0) + record["height"]
    count_by_name[first_name] = count_by_name.get(first_name, 0) + 1


for name, total in total_by_name.items():
    print(name, total / count_by_name[name])