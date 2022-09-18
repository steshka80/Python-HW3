# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

x = int(input("введите значение n : ")) 
def dec_to_bin (num):
    result = ""
    if num != 0:
        while num >= 1:
            result=result+str(num % 2)
            num = num // 2
        if num == 1:
            result = result + str(num) 
    else:
        result="0"   
    return (result)
def str_rev(str):
    main_result=""
    for i in range (len(str)-1,-1,-1):
        main_result = main_result+str[i]
    return main_result
print(str_rev(dec_to_bin(x)))
