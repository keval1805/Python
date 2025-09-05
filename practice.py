list1=[]
for j in range(1,6):
    list=input(" ")
    list1.append(list)

int_list=[]
float_list=[]
string_list=[]

for j in list1:
    if type(j)==int:
        int_list.append(j)
    elif type(j)==float:
        float_list.append(j)
    elif type(j)==str:
        string_list.append(j)
print("int list= ",int_list)
print("float list= ",float_list)
print("str list= ",string_list)