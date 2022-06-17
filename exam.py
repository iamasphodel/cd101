import random
def generation_id(count):
    rnd_id = 0
    for i in range(count):
        rnd_id = str(random.randint(1,100)) + str(rnd_id)
    return rnd_id


customers = [{"id": "55555", "name": "Anne","age":21, "prods": ["water"]}, {"id": "656864", "name": "Alice","products": ["sugar"]}]
g = input('Do you want to buy something? ')
while g == 'Yes' or g == 'yes'or g =='y':
    prov = input("do you have an account? ")
    if prov == "yes" or prov == "Yes" or prov == "y":
        prov_id = input('Enter your id: ')
        if prov_id == 'exit':
            break
        for x in customers:
            if prov_id == x["id"]:
                new_prods= input("Choice a product: ")
                x["products"].append(new_prods)
                with open("text.txt", 'w') as f:
                    f.write("yo")
                    f.close()
                print(customers)
        else:
            print("error!! Please enter correct id! ")

    elif prov == "No" or prov == "no":
        cust_new = {}
        cust_new["id"] = generation_id(12)
        cust_new["name"] = input("Enter a name: ")
        cust_new["age"] = int(input("Enter your age: "))
        cust_new["prods"] = input("Choice a product: ").split(", ")
        customers.append(cust_new)
        print(customers)
        f=open("text.txt", 'w')
        for cust in customers:
             f.write("yo")
        f.close()
    elif prov == "exit":
        break
