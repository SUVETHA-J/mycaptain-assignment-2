list_1=[12,-7,5,64,-14]
list_2=[12,14,-95,3]
li=[]
li1=[]
def list1():
    for i in list_1:
        if(i>0):
            li.append(i)
    print(li)
def list3():
    for j in list_2:
        if(j>0):
            li1.append(j)
    print(li1)
print("for list1")
list1()
print("for list 2")
list3()

