
t1=[1,2,3,4,5,6,'a']
t2=[]
t3=[]
sum=0
multiplication=1

for i in t1:
    try:
        if i % 2 == 0:
            t2.append(i)
            sum=sum+i   
        else:
            t3.append(i) 
            multiplication=multiplication*i 
             
    except:
            print("not valid number:",i)    

print("even number is :",t2)
print("sum of even number :",sum)
print("odd number is :",t3)
print("multiplication of odd number:",multiplication)               