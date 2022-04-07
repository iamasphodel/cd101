#import random
#customers=["Peter", "Joe", "George"]

#id=random.randint(10, 100)
#rnd_customer=random.choice(customers)
#print(rnd_customer)

import random

def generate_id(count):
    rnd_id=0
    for i in range(count):
        rnd_id=str(random.randint(0, 9))+str(rnd_id)
    return rnd_id   

def greet(name):
    print(f"Hey, {name}")

def generate_name(names):
    
    rnd_n=random.choice(names)
    return rnd_n
