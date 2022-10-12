import random
temperature=random.randint(1,100)
print("temperature level",temperature)
humidity=random.randint(1,100)
print("humidity level",humidity)
if temperature in range(1,45,1):
            print(" low temperatures ")
            print("alaram is off")
elif temperature in range(46,100,1):
        print("high temperature")
        print("alaram is on")
if humidity in range(1,60,1):
    print("the humidity is normal")
else:
    print("the humidity is high")
