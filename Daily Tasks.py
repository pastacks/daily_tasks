

# I've no idea what I'm doing but it's gonna be good





# Realistically I don't have a set schedule yet, and I mostly work weekends.
# I bet theres a way I can import my schedule from the app "7 shifts," and not even have to input the day.
# Computers always know what day it is. So I should be able to just hit a button and print a to do list based
# on the day and time, and perhaps even have a button for something on a weekly level.

# side note: I'm still having a hard time getting functions and parameters figured out, I will practice that more this week.




# #
# result_workday = ("Daily Tasks (WORKDAY): \n"
#                   "PHYSICAL ACTIVITY: \n"
#                   "Run with Jack\n"
#                   "Push ups or squats\n"
#                   "HYGIENE: \n"
#                   "Shower\n"
#                   "Lessons: \n"
#                   "Duolingo Spanish\n"
#                   "Write and Edit code\n"
#                   "Watch a bartending video\n"
#                   "Work")
#
#
# result_offday = ("Daily Tasks (DAY OFF): \n"
#                   "Run and/or walk with Jack\n"
#                   "Push ups or squats\n"
#                   "HYGIENE: \n"
#                   "Shower, cut nails etc.\n"
#                   "LESSONS: \n"
#                   "Duolingo Spanish\n"
#                   "Write and Edit code \n"
#                   "Watch a bartending video\n"
#                   "OTHER: \n"
#                   "Watch news\n"
#                   "Play Video Games or watch movies or hang out with friends")
#
# today = input("What is today?: ")
#
#
#
#  iftoday in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
#         print(result_workday)
# elif today in ("Saturday", "Sunday"):
#         print(result_offday)


# work_schedule = "What is your schedule like?: "


# def work_schedule():
#
def chore_list(today):
    if today in ("Sunday", "sunday"):
        print("Relax after church")
    elif today in ("Monday", "monday"):
        print("Exercise, cook, clean, work")
    elif today in ("Tuesday", "tuesday"):
        print("Exercise, cook, clean, work")
    elif today in ("Wednesday", "wednesday"):
        print("Exercise, cook, clean, work")
    elif today in ("Thursday", "thursday"):
        print("Exercise, cook, clean, work")
    elif today in ("Friday", "friday"):
        print("Exercise, cook, clean, work")
    elif today in ("Saturday", "saturday"):
        print("Relax")




chore_list(input("What is today?: "))


# def steam(games):
#     if games in ("among us", "Among Us"):
#         print("Sus")
#     elif games in ("Modern Warfare", "CoD"):
#         print("Not enough hard drive space")
#

# steam(input("What should we play?: "))
### saving some of this below to show you my thought process ###

# def chore_list_Monday():
#     Monday = "Exercise, cook, clean, work"
#
# def chore_list_Tuesday():
#     Tuesday = "Exercise, cook, clean, work"
#
# def chore_list_Wednesday():
#     Wednesday = "Exercise, cook, clean, work"
#
# def chore_list_Thursday():
#     Thursday = "Exercise, cook, clean, work"
#
# def chore_list_Friday():
#     Friday = "Exercise, cook, clean, work"
#
# def chore_list_Saturday():
#     Saturday = "Relax"



# chore_list_Sunday()



# Here's some new code I'm working on. Some sort of home-inventory grocery list

#
# def inventory(glist):
#
#
# glist = ["coffee", "tofu", "rice", "beans", ""]
# glist.append(input("Wtf else do we need?: "))
# glist.remove(input("What should we remove from the list?: "))