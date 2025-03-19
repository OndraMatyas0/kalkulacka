print("Vítejte v kalkulačce")

x=input("Zadejte první číslo ")
y=input("Zadejte druhý číslo ")

x=int(x)
y=int(y)



print("1 pro sčítání ")
print("2 pro odčítání ")
print("3 pro násobení ")
print("4 pro dělení ")
print("5 pro mocninu ")
print("6 pro odmocninu ")
print("____________________________________________________")
volba=input("Vyberte matematickou operaci-")


print("____________________________________________________")
if volba == "1":
    print(x+y)
elif volba == "2":
    print(x-y) 
elif volba == "3":
    print(x*y) 
elif volba == "4":
    if y == 0:
        print("Nejsi Chuck Norris")
else:
    print(x/y)
if volba == "5":
    print(x**y) 
elif volba == "6":
    print(x**(1/y))