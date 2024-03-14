import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.csv_reader(source_path)

    def csv_reader(self, source_path: str):
        with open(source_path, newline="") as csvfile:
            dishes = {}
            reader = csv.DictReader(csvfile)

            for row in reader:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = Ingredient(row["ingredient"])
                recipe_amount = int(row["recipe_amount"])

                if dish not in dishes:
                    dishes[dish] = Dish(dish, price)
                dishes[dish].add_ingredient_dependency(
                    ingredient, recipe_amount
                )
        return set(dishes.values())


""""""
