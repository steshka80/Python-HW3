# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

my_list=[1.1, 1.2, 3.1, 5, 10.01]

def find_max (my_list):
    max=round(my_list[0]%1,2)
    for i in my_list:
        if (i%1) > max:
            max = (i%1)
            max = round (max, 2)
    return(max)
def find_min (my_list):
    min=1-round(my_list[0]%1,2)
    for i in my_list:
        if (i%1) < min:
            min = (i%1)
            min = round (min, 2)
    return(min)

result = (find_max(my_list)) - (find_min(my_list))
print (f"результат = {result}")
