
#podtawowa składnia: (ta wyrzuca kwadrat danej liczby)
def square(x):
    return x ** 2
#wywołanie funkcji SQUARE

y = square(3)
print(y)

y = square(x=3)
print(y)

#nowa fukcja POWER
def power (exponent, base):
    return base ** exponent

print(power(2, 3))
print(power(exponent=2, base=3))
print(power(base=3, exponent=2))

print(power(2, base=3)) #OK
print(power(base=2, 2)) #ŹLE


