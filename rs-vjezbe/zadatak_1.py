broj1 = float(input("Unesite prvi broj: "))
operator = input("Unesite operator (+, -, *, /): ")
broj2 = float(input("Unesite drugi broj: "))

if operator == "+":
        rezultat = broj1 + broj2
        print(rezultat)
elif operator == "-":
        rezultat = broj1 - broj2
        print(rezultat)
elif operator == "*":
        rezultat = broj1 * broj2
        print(rezultat)
elif operator == "/":
        if broj2 == 0:
            print("Dijeljenje s nulom nije dozvoljeno!")
        else:
            rezultat = broj1 / broj2
            print(rezultat)
else:
        print("Nepodržani operator!")
