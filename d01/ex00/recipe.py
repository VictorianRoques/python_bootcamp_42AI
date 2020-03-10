class Recipe: #definition de la class Recipe
    """ Class definissant une recette caracterise par :
    - name
    - cooking_lvl (int) 1 to 5
    - cooking_time (int) in minute (no neg)
    - ingredients (list): list of all ingredients represented by a string
    - description (str): description of the recipe
    - recipe_type (str): can be "started", "lunch", or "dessert"""

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, description=""): #methode constructeur
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        self.handle_error()
    def __str__(self):
        txt = "Recipe {}: \n cooking_lvl = {}\n cooking_time = {}\n ingredients = {}\n recipe_type = {}\n description = {}"\
        .format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.recipe_type, self.description)
        return txt
    
    def handle_error(self):
        
        if type(self.name) is not str:
            return (print("ERROR Name is not a string"))
        if type(self.cooking_lvl) is not int:
            return (print("ERROR cooking_lvl is not an int"))
        if self.cooking_lvl < 1 or self.cooking_lvl > 5:
            return (print("ERROR cooking_lvl is not between 1 and 5"))
        if type(self.cooking_time) is not int:
            return (print("ERROR Cooking lvl is not INT"))
        if type(self.ingredients) is not list:
            return (print("ERROR ingredients is not a list"))
        if type(self.recipe_type) is not str:
            return (print("ERROR recipe_type is not a string"))
        return 0