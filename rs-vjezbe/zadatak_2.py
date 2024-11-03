godina = int(input("Unesite godinu: "))

if godina % 400 == 0 or (godina % 4 == 0 and godina % 100 != 0): 
    print("Godina", godina,"je prijestupna!")
else:
    print("Godina", godina,"nije prijestupna!")
