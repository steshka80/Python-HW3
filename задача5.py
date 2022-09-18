# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input("введите значение k : ")) 
array=[]
array.append(0)
array.append(1)
array.insert(0,-1)
def Fibonachi (x):
    index =- 1
    for i in range (2, x+1):
        array.append(array[i*2-2] + array[i*2-3])
        array.insert(0,(abs(array[0]) + abs(array[1])) * index)
        index = index*-1
    print(array)
Fibonachi(k)

