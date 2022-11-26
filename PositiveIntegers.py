n=int(input("Enter no. of elements to be present:"))
list1=[]
print("Enter elements:")
for i in range(0,n):
    a=int(input())
    list1.append(a)
pos=[]    
for i in range(0,n):
    if list1[i]>=0:
        pos.append(list1[i])
print(pos) 
