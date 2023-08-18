import pytest
from src.item import Item
from src.phone import Phone

def test_phone_creation():
    phone = Phone("iPhone", 999.99, 10, 1)
    assert phone.name == "iPhone"
    assert phone.price == 999.99
    assert phone.quantity == 10
    assert phone.number_of_sim == 1

def test_phone_addition():
    phone1 = Phone("iPhone", 999.99, 10, 1)
    phone2 = Phone("Samsung", 799.99, 5, 2)
    result = phone1 + phone2
    assert result == 15

def test_phone_addition_with_item():
    phone = Phone("iPhone", 999.99, 10, 1)
    item = Item("Charger", 19.99, 5)
    result = phone + item
    assert result == 15

def test_phone_invalid_number_of_sim():
    with pytest.raises(ValueError):
        Phone("iPhone", 999.99, 10, 0)

def test_phone_invalid_addition():
    with pytest.raises(TypeError):
        phone = Phone("iPhone", 999.99, 10, 1)
        phone + "Samsung"