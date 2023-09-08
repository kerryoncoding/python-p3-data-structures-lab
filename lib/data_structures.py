spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food_name["name"] for food_name in spicy_foods]
    #returns list of strings

def get_spiciest_foods(spicy_foods):
    new_list = [item for item in spicy_foods if item["heat_level"] >5]
    return new_list
    #returns list of dictionaries

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f'{item["name"]} ({item["cuisine"]}) | Heat Level: {"🌶"*item["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"]== cuisine:
            return item

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item["heat_level"] > 5:
            print(f'{item["name"]} ({item["cuisine"]}) | Heat Level: {"🌶"*item["heat_level"]}')

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
