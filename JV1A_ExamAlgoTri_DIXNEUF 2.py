#exercice 2

myTable =  [5, 9, 16, 10, 20]
comparateur = myTable[0]
indiceComparateur =0
stock = 0
print(myTable)

for i in range (len(myTable)):
    if (myTable[i]>comparateur):
        comparateur = myTable[i]
        indiceComparateur = i
    
stock = myTable[indiceComparateur]
myTable[indiceComparateur] = myTable[4]
myTable[4] = stock

print(myTable)
