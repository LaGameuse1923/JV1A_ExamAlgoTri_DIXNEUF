
#exercice 3

myTable =  [3, 9, 2, 5, 10]
comparateur = myTable[0]
indiceComparateur =0
stock = 0
cpt = 0
j = 0

for i in range (4):
    
    comparateur = myTable[i]
    
    for j in range(i,len(myTable)):
        if (myTable[j]<comparateur):
            comparateur = myTable[j]
            indiceComparateur = j


    stock = myTable[indiceComparateur]
    myTable[indiceComparateur] = myTable[i]
    myTable[i] = stock
 
    print(myTable)





   

    #stock = myTable[cpt]
    #print(stock)
    #myTable[cpt] = myTable[indiceComparateur]
    ##print(myTable[indiceComparateur])
    #myTable[indiceComparateur]= stock
    #print(myTable[cpt])

print(myTable)

"""

stock = myTable[cpt]

myTable[cpt] = myTable[indiceComparateur]

myTable[indiceComparateur]= stock


"""