"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.phone import Phone
from src.item import Item, InstantiateCSVError


def test_calculate_total_price():
    item = Item("Test item", 10, 5)
    assert item.calculate_total_price() == 50


def test_apply_discount():
    item = Item("Test item", 10, 5)
    item.apply_discount()
    assert item.price == 10 * item.__class__.pay_rate


def test_name():
    item: Item = Item("Item 3", 30.0, 1)
    assert item.name == "Item 3"


def test_name_setter():
    item = Item("Item 4", 40.0, 3)
    item.name = "Item 4 Updated"
    assert item.name == "Item 4 Upd"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

