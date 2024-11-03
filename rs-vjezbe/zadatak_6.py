for i in range(1, 2):
print(i)
# nema smisla jer se ispuje samo 1 (jer je raspon od 1 do 2, a 2 se ne ispisuje), pa ni nema potrebe za korištenjem petlje

for i in range(1, 10, 2):
print(i)
# ispisuje 1,3,5,7,9 (od 1 i uvećava se za 2)

for i in range(10, 1, -1):
print(i)
# ispisuje se 10,9,8,7,6,5,4,3,2 (-1 znači da se umanjuje svaki puta za 1, a kreće se od 10)