
#Daily Tasks WebApp Project


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