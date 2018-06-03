
x = float(input("Wpisz liczbę x: "))
y = float(input("Wpisz liczbę y: "))
print(x)
print(y)
liczba = input("Wybierz liczbę z podanego przedziału: ")
print(liczba)
rand = random.randint(x ,y)


while liczba != rand:
    if liczba < rand:
        print("ta liczba jest za mała. podaj kolejną.")
        print(input("Wpisz liczbę z podanego zakresu:"))
    else liczba > rand:
        print("ta liczba jest za duża. podaj kolejną.")
        print(input("Wpisz liczbę z podanego zakresu:"))
    print ("Zgadłeś!")


#####################################


import random

lower_bound = int(input("Podaj dół zakresu: "))
upper_bound = int(input("Podaj górę zakresu: "))

target = random.randint(lower_bound, upper_bound)

guess = None
count = 0

while target != guess:
    count += 1
    guess = int(input("Podaj liczbę: "))
    if guess < target:
        print("Za mało!")
    elif guess > target:
        print("Za dużo")
print("Gratulacje! ilość ruchów: ", count)