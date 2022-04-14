import random

# user_info=("Enter your name, lastname, year using comma: ").split(",")
# print(user_info[])
dict = {"id": "124fasf", "name": "Azamat", "age": 12, "products": ["pepsi", "water", "chocloate"]}
lst = ["Aazamat", 12, "pepsi"]

customers = []


d = {}
lst = []

lst.append("Petya")
d["name"] = "Ivan" # d = {"name": "Ivan"}
d["name"] = "Katya" # d = {"name": "Katya"}

print(d["name"]) # Katya

customers.append(d) # customers = [{"name": "Ivan"}]

customers.append(d) # customers = [{"name": "Ivan"}, {"name": "Ivan"}]

user=input("Do you have an id? (yes=1, no=0): ")
if int(user)==1:
    print("нужно искать id в словаре ")
if int(user)==0:
    user_name = input("Please, enter your name: ")
    print("Hello, " + user_name)    
    user_age=input("Please, enter your age: ")   
    
    hash = random.getrandbits(128)
    print("Hello, " + user_name)
    print("your id is: %0.32x" % hash)
  


# ключ и значение. элемент это пара из ключа и значений 
# создаю ключ олни и те же но значения разные 


choice=input("What would you want to buy: ")
    






