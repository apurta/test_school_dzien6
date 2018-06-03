
import random

print(random.random) #zwraca jedna losowa liczbe z przedziału <0,1)
print(random.randint(0, 10)) # od 0 do 10 włącznie
print(random.choice(["a", "b", "c"])) # losowa liczba z listy

def foo():
    print("foo")

def bar():
    print("bar")

func = random.choice([foo.bar])
func()

if random.random() < 0.5:
    foo()

#############################

