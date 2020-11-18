
#Daily Tasks WebApp Project

work_schedule={
    "Sunday":["1100 - 1900"],
    "Monday":["Off"],
    "Tuesday":["1000 - TBD"],
    "Wednesday":["1000 - TBD"],
    "Thursday":["1000 - TBD"],
    "Friday":["1200 - 2000"],
    "Satuday":["1100 - 2100"],
    }

def print_schedule():
    for key in work_schedule:
        print_times(key)


def print_times(key):
        work_times = work_schedule.get(key)
        print(work_times)


def get_input(message):
    user_input = input(message)
    return user_input


if __name__ == "__main__":
    for key in work_schedule:
        message = f"Enter the day: "
        print_times(key)
        when_to_work = get_input(message)
    print_times()
