
# Grocery List WebApp project

grocery_dict={
    "dry":["Beans", "Rice", "Spices", "Granola", "Poptarts", "Tortillas", "Oil", "Noodles", "Bread", "Oats"],
    "fridge":["Milk", "Sauce", "Hummus", "Tofu", "Jelly", "Veggie broth", "Spinach"],
    "frozen":["Potatoes", "Veggies"],
    "misc":["Soap", "Sponges", "Broom"],
    }

#
def dry_base():
    dry = grocery_dict.get("dry")
    dry.sort()
    print(dry)

def fridge_base():
    fridge = grocery_dict.get("fridge")
    fridge.sort()
    print(fridge)

def frozen_base():
    frozen = grocery_dict.get("frozen")
    frozen.sort()
    print(frozen)

def misc_base():
    misc = grocery_dict.get("misc")
    misc.sort()
    print(misc)


dry_base()
fridge_base()
frozen_base()
misc_base()


# Now attempting the dictionary version of this #
