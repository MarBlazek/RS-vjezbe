def provjera_lozinke(lozinka):
    
    if len(lozinka) < 8 or len(lozinka) > 15:
        return "Lozinka mora sadržavati između 8 i 15 znakova."
    
    ima_veliko_slovo = False
    ima_broj = False
    
    for char in lozinka:
        if char.isupper():
            ima_veliko_slovo = True
        if char.isdigit():
            ima_broj = True
    
    if ima_veliko_slovo == False or ima_broj == False:
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj."
    
    lozinka_lower = lozinka.lower()
    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'."
    
    return "Lozinka je jaka!"

lozinka = input("Unesite lozinku: ")

print(provjera_lozinke(lozinka))