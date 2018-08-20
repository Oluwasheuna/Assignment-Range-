import random
import math
for i in range (5):
    a = random.randint(1,100)
    b = int(input("Type any number of your chooice: "))
    if a == b:
        print("Correct!, my choice was ", a)
    elif abs(a - b)<= 10:
        print("You are close, my choice was ", a)
    else:
        print("You are not even close, my choice was ", a)
    
