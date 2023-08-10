"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


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


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) > 0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
