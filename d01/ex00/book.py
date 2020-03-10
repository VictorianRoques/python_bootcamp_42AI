import time
from recipe import Recipe
from datetime import date, datetime
class Book:
    def __init__(self, name: str, recipes_list: dict):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        for x in self.recipes_list:
           for y in self.recipes_list[x]:
               if name == y.name:
                   return (print(y.__str__()))
        return print ("{} NOT FOUND".format(name.upper()))
    
    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list.keys():
            return (print("Sorry we dont have {} recipe".format(recipe_type)))
        print ("{} recipe that you can do:".format(recipe_type))
        for x  in self.recipes_list.get(recipe_type):
            print (" {}".format(x.name))

    def add_recipe(self, recipe: Recipe):
        if (type(recipe) is not Recipe):
            return (print("ERROR this not a validate Recipe"))
        if recipe.recipe_type not in self.recipes_list.keys():
            return (print("ERROR {} is not a type of lunch".format(recipe.recipe_type)))
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
            