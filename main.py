#Задание 22
x1=int(input("Введите количество элементов первого множества: "))
x2=int(input("Введите количество элементов второго множества: "))
list_1=[]
list_2=[]
for i in range(0,x1):
    number = int(input(f"Введите элемент 1 множества(еще {(x1-i)} ): "))
    list_1.append(number)
print("Первое множество чисел: ")
print(list_1)
for y in range(0,x2):
    number = int(input(f"Введите элемент 2 множества(еще {(x2-y)} ): "))
    list_2.append(number)
print("Второе множество чисел: ")
print(list_2)
list_1=list(set(list_1))
list_2=list(set(list_2))
list_3=[]
for i in range(0,len(list_1)):
    for y in range(0,len(list_2)):
        if list_1[i]==list_2[y]:
            list_3.append(list_1[i])
print(list_3)
numberX=list_3[0]
for y in range(0,x1+x2):
    for i in range(0,len(list_3)):
        if i!=0:
            if list_3[i]<list_3[i-1]:
                numberX=list_3[i]
                list_3[i]=list_3[i-1]
                list_3[i-1]=numberX
print(list_3)

#задание 24
number24=int(input("Введите количество кустов: "))
num24=[]
for i in range(0,number24):
    number = int(input(f"Введите сколько ягод выросло (еще {(number24-i)} ): "))
    num24.append(number)
max=0
for i in range (0,len(num24)):
    if i !=0 and i != len(num24) and i != len(num24)-1 and i !=len(num24)-2:
        sum=int(num24[i]+num24[i+1]+num24[i+2])
        if max<sum:
            max=sum
    else:
        sum=int(num24[0]+num24[len(num24)-1]+num24[len(num24)-2])
        if sum > max:
            max=sum
        
print(max)