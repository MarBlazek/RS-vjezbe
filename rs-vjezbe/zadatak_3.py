tajni_broj = 26

brojač = 0

print ("Pogodite broj u rasponu od 1 do 100: ")

while True:
    broj = int(input("Pogodi broj! "))
    brojač += 1
    if broj < tajni_broj:
        print("Broj je veći od vaše pretpostavke.")
    elif broj > tajni_broj:
        print("Broj je manji od vaše pretpostavke.")
    else:
        print("Bravo, pogodio si u", brojač, "pokušaja!")
        break