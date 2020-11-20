#This will be a roll the dice game for D&D or something


import random

#4
def roll_4():
    roll = random.randit(1,4)
    print(roll)

# 6
def roll_6():
    roll = random.randint(1,6)
    print(roll)

# 8
def roll_8():
    roll = random.randit(1,8)
    print(roll)

# 10
def roll_10():
    roll = random.randit(1,10)
    print(roll)

# 10 (00-90)
def roll_10_0():
    roll = random.randit(00,90)
    print(roll)

# 12
def roll_12():
    roll = random.randit(0,12)
    print(roll)


# 20
def roll_20():
    roll = random.randint(1,20)
    print(roll)

def output():
    dnum = print(input("Roll?: "))
    if dnum in ("4"):
        roll_4
    

output()











# while (input("Roll: ") in (6)

# if input("Roll: ") in (8)
#     roll_8()

# if input("Roll: ") in (20):
#     roll_20()