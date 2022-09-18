# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_list=[2, 3, 5, 9, 3]
def main_task (my_list):
    sum=0
    for i in range (1, len(my_list), 2):
        sum = sum + my_list[i]
    return(sum)
print (f"Сумма элементов на нечетных позициях = {main_task(my_list)}")



