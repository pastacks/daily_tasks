#!/usr/bin/env python

# Grocery List WebApp project

grocery_dict={
    "dry":["Beans", "Rice", "Spices", "Granola", "Poptarts", "Tortillas", "Oil", "Noodles", "Bread", "Oats"],
    "fridge":["Milk", "Sauce", "Hummus", "Tofu", "Jelly", "Veggie broth", "Spinach"],
    "frozen":["Potatoes", "Veggies"],
    "misc":["Soap", "Sponges", "Broom"],
    }

def print_groceries():
    for key in grocery_dict:
        print_grocery_section(key)

def print_grocery_section(key):
        section_list = grocery_dict.get(key)
        section_list.sort()
        print(section_list)

def update_list(key, items):
    grocery_copy = grocery_dict.copy()
    for i in items:
        grocery_copy[key].remove(i)

def get_input(message):
    user_input = input(message)
    return user_input.split(', ')


if __name__ == "__main__":

    for key in grocery_dict:
        message = f"what do you already have in the {key} list?"
        print_grocery_section(key)
        what_we_got = get_input(message)
        update_list(key, what_we_got)
    print_groceries()