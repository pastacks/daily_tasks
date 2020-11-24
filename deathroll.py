#This will be a roll the dice game for D&D or something


import random

#2
def coin_flip():
    flip = random.randint(1,2)
    return flip


#4
def D4():
    roll = random.randint(1,4)
    return roll

# 6
def D6():
    roll = random.randint(1,6)
    return roll

# def double_six():
#     roll_1 = random.randint(1,6)
#     roll_2 = random.randint(1,6)
#     return 

# 8
def D8():
    roll = random.randint(1,8)
    return roll

# 10
def D10():
    roll = random.randint(1,10)
    return roll

# 10 (00-90)
def D00():
    roll = random.randint(1,10) 
    return roll

# 12
def D12():
    roll = random.randint(1,12)
    return roll


# 20
def D20():
    roll = random.randint(1,20)
    return roll


# output
def output():
    dnum = input ("Action: ")
    if dnum in ("/roll D4"):
        print(D4())
    if dnum in ("/roll 2D4"):
        print(D4())
        print(D4())
    if dnum in ("/roll 3D4"):
        print(D4())
        print(D4())
        print(D4())
    if dnum in ("6"):
        print(D6())
    # if dnum in ("double six"):
    #     print(double_six())
    if dnum in ("8"):
        print(D8())
    if dnum in ("10"):
        print(D10())
    if dnum in ("00"):
        print(D00())
    if dnum in ("12"):
        print(D12())
    if dnum in ("20"):
        print(D20())
    if dnum in ("Flip", "flip"):
        print(coin_flip())
    return dnum
            
    
output()

