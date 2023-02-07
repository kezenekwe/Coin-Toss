import random

active = True
while active:
    toss = input("Press Y to toss a coin. Press N to decline. ")
    if toss.lower() == 'y':
        rand_num = random.randint(0, 1)
        if rand_num == 0:
            print("You got heads")
            retoss = input("Roll again? (Y/N): ")
            if retoss.lower() == "y":
                active = True
            else:
                active = False
                print("Thank you for playing.")
        if rand_num == 1:
            print("You got tails.")
            retoss = input("Roll again? (Y/N): ")
            if retoss.lower() == "y":
                active = True
            else:
                active = False
                print("Thank you for playing.")
    elif toss == 'n':
        active = False
        print("Thank you for playing")


