#This will be a roll the dice game for D&D or something


import random

#2
def coin_flip():
    flip = random.randint(1,2)
    print(flip)


#4
def roll_4():
    roll = random.randint(1,4)
    print(roll)

# 6
def roll_6():
    roll = random.randint(1,6)
    print(roll)

# 8
def roll_8():
    roll = random.randint(1,8)
    print(roll)

# 10
def roll_10():
    roll = random.randint(1,10)
    print(roll)

# 10 (00-90)
def roll_00():
    roll = random.randint(00,90)
    print(roll)

# 12
def roll_12():
    roll = random.randint(0,12)
    print(roll)


# 20
def roll_20():
    roll = random.randint(1,20)
    print(roll)



# output
def output():
    dnum = input("Roll:? ")
    if dnum in ("4"):
        print(roll_4())
    if dnum in ("6"):
        print(roll_6())
    if dnum in ("8"):
        print(roll_8())
    if dnum in ("10"):
        print(roll_10())
    if dnum in ("00"):
        print(roll_00())
    if dnum in ("12"):
        print(roll_12())
    if dnum in ("20"):
        print(roll_20())
            
output()

