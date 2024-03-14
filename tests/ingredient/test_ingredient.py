from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("sugar")
    hash1 = hash(ingredient1)
    ingredient2 = Ingredient("coffee")
    hash2 = hash(ingredient2)
    assert ingredient1.name == "sugar"
    assert ingredient2.name == "coffee"
    assert ingredient1.__hash__() == hash1
    assert ingredient2.__hash__() == hash2
    assert ingredient1.__hash__() != ingredient2.__hash__()
    assert ingredient1.__repr__() == "Ingredient('sugar')"
    assert ingredient1.__eq__(ingredient2) is False
    assert ingredient1.__eq__(ingredient1) is True
    assert ingredient1.restrictions == set()
