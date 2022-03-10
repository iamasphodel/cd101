#input()

#print()

#int()/str()

#len()
#у функции есть круглые скобки и имя. Выше перечисленные это абстракции, т.е. вызов уже существующих функций
# 
#Создаем свою функцию:
# def shop():
#     c = input("Enter yu name: ")
#     print(f'Hello, {c}')
# shop()    

# def Age():
#     a = input("Enter ur age: ")
#     if int(a)>=18: 
#       print("Вы совершеннолетний")
#     else:
#        print("Вы несовершеннолетний")  
# Age()        

# def shop(c, age):
#     print(f'Hello, {c}, {age}')
# shop("Alice", 23)    

#после выполнения функции с обнуляется 
# def sum_two(a,b):
#     c=a+b
#     print(c)
# sum_two(5,9)

# #Можем исподльзовать с в других операциях. Сохранили значение суммы в переменной с
# def sum_two(a,b):
#     return a+b
# c=sum_two(5,9)

arr=[1,5,9,8,7,6]
def sum_ar(arr):
    summ=0
    for z in arr:
        summ=summ+z
    return summ    
s=sum_ar(arr)
print(s)