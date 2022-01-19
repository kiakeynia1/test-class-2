import random
    
computer = random.randint(0, 20)
c = 0 
while True:

    user = int(input(""))
    c = c + 1

    if user == computer:
        print("barande shodi!!")
        print(c)
        break

    elif user > computer:
        print("paeentar")

    elif user < computer:
        print("balatar")

