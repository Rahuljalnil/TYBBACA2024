t=(1,2,3,4,1,6,8,5,4,2)
print(t)
list=[]
print("repeated elements in given tuple")
for i in range(0,len(t)):
    if t.count(t[i])>1:
        if t.count(t[i])>1:
            if t[i] not in list:
                list.append(t[i])
                print(t[i])