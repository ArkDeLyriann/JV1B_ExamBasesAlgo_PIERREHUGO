#PARTIE 1 - TRI A BULLES
import random

myTable = [0,0,0,0,0]

for i in range (0,len(myTable)):
    myTable[i]=random.randint(0,100)

print(myTable)

for j in range (0, len(myTable)):
    for k in range(j, len(myTable)):
        if (myTable[j]>myTable[k]):
            stock = myTable[k]
            myTable[k] = myTable[j]
            myTable[j] = stock


print(myTable)




