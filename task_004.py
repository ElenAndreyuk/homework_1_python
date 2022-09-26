# Напишите программу, которая по заданному 
# номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).


try:
    quarter = int (input('введите номер четверти: '))
    if quarter == 1:
        print ('x > 0 и y > 0')
    elif quarter == 2:
        print ('x < 0 и y > 0')
    elif quarter == 3:
        print ('x < 0 и y < 0')
    elif quarter == 4:
        print ('x > 0 и y < 0') 
    else : print ('некорректный ввод')       
except:
    print ('некорректный ввод')      
