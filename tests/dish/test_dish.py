from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish1 = Dish("salad", 5.00)
    dish2 = Dish("salad", 5.00)
    dish3 = Dish("espaguete", 10.00)
    assert dish1.name == "salad"
    assert dish1.__hash__() == dish2.__hash__()
    assert dish1.__hash__() != dish3.__hash__()
    assert dish1.__eq__(dish1) is True
    assert dish1.__repr__() == "Dish('salad', R$5.00)"
    with pytest.raises(TypeError, match="Dish price must be float."):
        dish_error = Dish("salad", "5.00")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        dish_error = Dish("salad", -1)
        dish_error

    assert dish1.get_ingredients() == set()
    assert dish1.get_restrictions() == set()
    dish1.add_ingredient_dependency("queijo mussarela", 5)
    assert dish1.get_ingredients() == {"queijo mussarela"}
