import sys
cookbook = {
    'sandwich' : {  'ingredients' :['ham', 'bread', 'cheese', 'tomatoes'],
                    'meal' : 'lunch',
                    'prep_time' : '10'},
    'cake' : { 'ingredients' : 'flour, sugar, eggs',
                'meal' : 'dessert',
                'prep_time' : '60'},
    'salad' : { 'ingredients' : 'avocado, arugula. tomatoes, spinach',
                'meal' : 'lunch',
                'prep_time' : '15'}
    }

def     write_recipe(recipe_name):
    if (recipe_name in cookbook):
        print("Recipe for {}".format(recipe_name))
        print("Ingredients list: {}".format(cookbook[recipe_name]['ingredients']))
        print("to be eaten for {}".format(cookbook[recipe_name]['meal']))
        print("Takes {} minutes of cooking".format(cookbook[recipe_name]['prep_time']))
    else:
        print("Sorry {} doesn't seem to exist, do you want to create it ?".format(recipe_name))

def     add_recipe(recipe_name, ingredients, meal, prep_time):
    if (recipe_name in cookbook):
        print("This {} already exist".format(recipe_name))
    else:
        cookbook[recipe_name] = { 'ingredients' : ingredients, 'meal' : meal, 'prep_time': prep_time}
        print("{} recipe succefuly add to the cookbook".format(recipe_name))

def     delete_recipe(recipe_name):
    if (recipe_name in cookbook):
        del cookbook[recipe_name]
        print("{} recipe have been delete".format(recipe_name))
    else:
        print("{} recipe doesn't seem to exist")

def     print_cookbook():
   print(cookbook)

def start():
    print("PLease select an option by typing the corresponding number")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: print the cookbook")
    print("5: Quit")

    y = int(input())
    if (y == 1):
        write_recipe(y)
    elif (y == 2):
        delete_recipe(y)
    elif (y == 3):
        add_recipe(y)
    elif(y == 4):
        print_cookbook
    elif y == 5:
        exit()
    else:
        print("please enter a valid input")
        y = int(input())

start()