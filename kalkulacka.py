print("vítejte v programu karkulačka")

x = int(input("Zadejte proměnnou x "))
y = int(input("Zadejte proměnnou y "))
print("Zde máte na výběr z následující nabídky: ")

print("1. Sčítání zadejte- 1")
print("2. odčítání zadejte- 2")
print("3. násobení zadejte- 3")
print("4. dělení zadejte- 4")
print("5. mocnění zadejte- 5")
print("6. odmocnění zadejte- 6")

operator = input("Zadejte volbu matematicé operace:")

if operator == "1":
    print(x+y)
elif operator == "2":
    print(x-y)
elif operator == "3":
    print(x*y)
elif operator == "4":
    if y == 0:
        print("Nejsi chuck Norris")
    else:
        print(x/y)
elif operator == "5":
    print(x**y)
elif operator == "6":
    print(x**(1/y))
else:
    print("Nezvolil jsi správnou operaci")

