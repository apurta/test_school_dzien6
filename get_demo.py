example = {"a":1, "b":2, "c":3}

print(example["a"])  #wydr to co odp kluczowi a

print(example.get("d", 5)) #gdy nie mamy takiego klucza jak "d"
print(example.get("d"))


# ex2

demo = {"a": [1,2,3], "b":[4,5,6]}
demo["a"].append(5)
#to samo co wyżej
lista = demo["a"]
lista.append(5)
