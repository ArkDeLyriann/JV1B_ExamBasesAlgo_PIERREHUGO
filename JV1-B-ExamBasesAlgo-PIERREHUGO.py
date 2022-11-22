#PARTIE 1 - TRI A BULLES
import random

myTable = [0,0,0,0,0]

for i in range (0,len(myTable)):
    myTable[i]=random.randint(0,100)

print(myTable)

#Ex 1 /

#stock = myTable[2]
#myTable[2] = myTable[4]
#myTable.pop(4)
#myTable.insert(4,stock)

#print(myTable)

#Ex 2 /
comparateur = 999

for j in range (0, len(myTable)):
        if (myTable[j]>myTable[j+1]):
            stock = myTable[j]
            
            myTable[j+1] = myTable[j]
            myTable.pop(j+1)
            myTable.insert(j+1,stock)

print(myTable)