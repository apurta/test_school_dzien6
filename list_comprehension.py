
#petli for używa sie do tworzenia listy -> iteruje po kolei i coś z tym robie
#specjalna składnia gdzoie można for zamnknąć w def listy
#

dev_ids = []

for i in range(1,5):
    dev_ids.append("device_" + str(i))

#ALBO

print(dev_ids)
print(["device_" + str(i) for i in range(1, 5)])

#liczba kwadratów pierwszych liczb naturalnych od 1 do 100

print()
print()

print([i**2 for i in range(1, 5)])

#tak to ma wyglądać
#data = [{"id": 1, "model": "AFGS"}, {..}, {..}]

#najpierw z pętlą FOR

data = [{"id": 1, "model": "ABD34"}, {"id": 2, "model": "AB4534"}, {"id": 3, "model": "ABRG34"}]

for record in data:
    print(record["id"])
#a teraz bez
print([record["id"] for record in data])


# zdef liste skład się z łzńcuch znaków etc. a potem wygenreuj liste
print()
texts = ['abc', 'gjkr', 'ghjs;g']
print([len(text) for text in texts])

