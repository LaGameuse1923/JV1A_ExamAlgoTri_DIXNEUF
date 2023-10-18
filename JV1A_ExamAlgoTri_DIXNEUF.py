#exercice 1

myTable =  [15, 9, 6, 10, 1]
stock = 0
print(myTable)

stock = myTable[0]
myTable[0] = myTable[4]
myTable[4] = stock

print(myTable)























































"""
myTable =  [10, 9, 16, 5, 20]
comparateur = myTable[0]
indiceComparateur =0
stock = 0
i = 0
cpt = 0







for i in range (len(myTable)):
    if (myTable[i]<comparateur):
     comparateur = myTable[i]
     indiceComparateur = i

   
   
   
    
    #print(comparateur)
    #print(indiceComparateur)
   
    stock = myTable[indiceComparateur]
   #print(stock)
    myTable[indiceComparateur] = myTable[cpt]
   #print(myTable[indiceComparateur])
    myTable[cpt] = stock
   #print(myTable[cpt])

         

    
     
     
     
     
     
   
        
        
       


   



            
            
print(myTable)    
"""