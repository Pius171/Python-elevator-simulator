import random

starting_floor =  random.randint(0,20) #generate a randon number from 0-20
floor=0
print("Welcome to floor {} ".format(starting_floor)) 

print("Hi {}, it's nice to have you here".format(input("What is your name? ")))

while True:
    try:
        answer =input("Are you going up or down: ").strip().lower()
        
        if answer == "up":
            num_floor = int(input("How many floors up? "))
            if (num_floor + starting_floor) > 20:
                print("stairs does not exist")
                raise Exception("")
            else:
                floor = starting_floor + num_floor

        if answer == "down":
            num_floor = int(input("How many floors down? "))
            floor = starting_floor - num_floor
            if floor < 0 :
                print("floor does not exist")
                raise Exception("")

            
        print("Hold on tight we are going {}\n\nwe started from floor {} and we have arrived at {} do have a nice day".format(answer,starting_floor, floor))
        break

    except:
        print("error invalid input")
        continue






