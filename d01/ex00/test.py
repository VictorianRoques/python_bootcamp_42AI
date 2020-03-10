from book import Book
from recipe import Recipe

sandwich = Recipe('sandwich', 1, 10, ['tomatoe', 'oignons', 'salad'], 'lunch', "un savoureux sandwich")
muesli = Recipe('muesli', 2, 5, ['flocons', 'lait'], 'dessert', "un beaux melange")
salad = Recipe('salad', 3, 15, ['avocado', 'ploplo', 'fraise'], "starter", "wahou")
dic = {'started': [salad], 'lunch': [sandwich], 'dessert': [muesli]}
livre = Book('Recette de Jean Michel', dic)
kebab = Recipe('kebab', 5, 30, ['tomatoe', 'oignons', 'salad', 'tofu'], 'lunch', "un savoureux mamene")

livre.add_recipe(kebab)
livre.get_recipes_by_types('lunch')
livre.get_recipe_by_name(sandwich.name)

livre.get_recipes_by_types('toto')
livre.get_recipe_by_name('yoyo')
livre.add_recipe("blablas")