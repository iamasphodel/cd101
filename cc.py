
#user_name=input("Please enter your name, age: ").split(", ")

#choise=input("Выберите кофе или сигареты (кофе=1, сигареты=0): ")
#if int(choise)==1:
#    print("Ваш заказ оформлен")
#if int(choise)==0:
#    if int(user_name[1])>=18: 
#        print("Ваш заказ оформлен")
#    else:
#        print("Отказ")    

#x=0
#while x<10:
#    print("Coffee or cigs")
#    x=x+1
#print("print out of loop") 


while True:
    choise=input("Cof(0), cig(1), ter(2)")
    if choise=="2":
        break

while True:
    choise=input("Cof(0), cig(1), ter(2)")
    if choise=="0":
        print("cof")
    elif choise=="1":
        print("cig")
    elif choise=="2":
        break
print("print out of loop") 

    