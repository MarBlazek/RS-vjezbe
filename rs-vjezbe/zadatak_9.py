def ukloni_duplikate(lista):
    bez_duplikata = list(set(lista))  
    return bez_duplikata  

lista = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7]
print(ukloni_duplikate(lista))