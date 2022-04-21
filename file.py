#1
#  import random

# f=open("text.txt", 'a')

# for i in range(10): 
#     rand=str(random.randint(10, 100))
#     f.write(str(rand))
#     f.write("\n")
# f.close()


# 2
# import random

# f=open("text.txt", 'a')
# for i in range(10): 
#     f.write(f"{random.randint(0, 9)}\n")
# f.close()


# 3
# users=["A\n", "B\n", "C\n", "D\n", "E\n"]
# f=open("text.txt", 'a')
# f.writelines(users)
# f.close()

# 4
# customers=[{"name": "Anne", "age":23},
#            {"name": "Alice", "age":25},
#            {"name": "Bob", "age":20}]

# f=open("text.txt", 'w')
# for customer in customers:
#      f.write(f"{customer}\n")
# f.close()

# 5
# customers=[{"name": "Anne", "age":23},
#            {"name": "Alice", "age":25},
#            {"name": "Bob", "age":20}]

# with open("text.txt", 'r+') as f:
#     for customer in customers:
#         f.write(f"{customer}\n")

# 6 все что прочитано с файла выводится в консоль
# with open("text.txt", 'r+') as f:
#     data=f.read()
#     print(data)

# # 7
# with open("text.txt", 'r+') as f:
#     data=f.readlines()
#     print(data)

# 8
# with open("text.txt", 'r+') as f:
#      data=f.readlines()
#      for line in data:
#          user=line.split(',')

#          customer={} #создаем словарь
#          customer["name"]=user[0]
#          customer["age"]=int(user[1].split("\n")[0])

#          print(customer)

# # 9 если у всех есть список продуктов
# customers=[]

# with open("text.txt", 'r+') as f:
#     data=f.readlines()
#     for line in data:
#         user=line.split(',')
#       
#         customer={} 
#         customer["name"]=user[0]
#         customer["age"]=int(user[1].split("\n")[0])
#         customer["products"]=user[2].split(";")

#         customers.append(customer)
#         print(customer)

#10 если у кого-то еще нет покупок
# customers=[]
#
# with open("text.txt", 'r+') as f:
#     data=f.readlines()
#     for line in data:
#         user=line.split(',')
#        
#         customer={} 
#         customer["name"]=user[0]
#         customer["age"]=int(user[1].split("\n")[0])
#         customer["products"]=user[2:] #начиная со значения с индексом 2
#
#         customers.append(customer)
#         print(customer)

