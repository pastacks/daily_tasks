#This will be a roll the dice game for D&D or something


import random

#2
def coin_flip():
    flip = random.randint(1,2)
    print("1 = Heads, 2 = Tails")
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

# I need to figure out how I can just put a command that runs the function a certain amount of times 
def output():
    cmd = input ("Action: ")
    if cmd in ("Flip", "flip"):
        print(coin_flip())
    if cmd in ("D4"):
        print(D4())
    if cmd in ("2D4"):
        print(D4())
        print(D4())
    if cmd in ("3D4"):
        print(D4())
        print(D4())
        print(D4())
    if cmd in ("6"):
        print(D6())
    # if cmd in ("double six"):
    #     print(double_six())
    if cmd in ("2D6"):
        print(D6())
        print(D6())
    if cmd in ("8"):
        print(D8())
    if cmd in ("10"):
        print(D10())
    if cmd in ("00"):
        print(D00())
    if cmd in ("12"):
        print(D12())
    if cmd in ("20"):
        print(D20())
    
            
    
output()

