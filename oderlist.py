l=[]
<<<<<<< Updated upstream
nbelt=input("give number of numbers you will put\n")
=======
list=[]
nbelt=input("give number of number you will put\n")
>>>>>>> Stashed changes
for i in range(int(nbelt)):
    nbr=input("give your number\n")
    l.append(int(nbr))

print("the list given",l)

for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i] > l[j]):
           temp=l[j]
           l[j]=l[i]
           l[i]=temp

list.append(l[0])
for i in range(1,len(l)):
    if(l[i]!=l[i-1]):
        list.append(l[i])
           
print("the list in order",list) 
