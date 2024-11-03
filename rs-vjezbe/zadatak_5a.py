broj = int(input("Unesite broj: "))

faktorijel = 1
i = 1  

while i <= broj:
    faktorijel *= i  
    i += 1 

print("Faktorijel broja", broj, "je:", faktorijel)