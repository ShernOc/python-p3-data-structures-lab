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
    return [items["name"] for items in spicy_foods]

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    # returns a list of dic where heat level of food is greater than 5 
    return [items for items in spicy_foods if items["heat_level"]>5]

print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for i in spicy_foods: 
        name = i["name"]
        cuisine = i["cuisine"]
        heat_level = int(i["heat_level"]) * "🌶"
        print (f"{name} ({cuisine}) | Heat Level: {heat_level}") 

print(print_spicy_foods(spicy_foods))
    
def get_spicy_food_by_cuisine(spicy_foods,cuisine):
    #return a single dictionary 
    for food  in spicy_foods:
        if food["cuisine"] == cuisine:
            print (food)
            return food
print(get_spicy_food_by_cuisine(spicy_foods,"Thai"))

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

print(print_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    #returns an integer representing the average heat level of all spicy food. 
    # average = total/total list 
    total = sum(i["heat_level"] for i in spicy_foods)    
    total_list = len((spicy_foods))
    average = int(total/total_list)
    return average
    
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    #list.append(): 
      spicy_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10, }
      spicy_foods.append(spicy_food)
      return spicy_foods
print(create_spicy_food(spicy_foods,spicy_foods))
