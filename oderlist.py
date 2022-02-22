l=[]
nbelt=input("give number of number you will put\n")
for i in range(int(nbelt)):
    nbr=input("give your number\n")
    l.append(int(nbr))
print("the list given",l)
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i] >= l[j]):
            temp=l[j]
            l[j]=l[i]
            l[i]=temp

print("the list in order",l)            

