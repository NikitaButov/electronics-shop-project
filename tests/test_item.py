"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item("Test item", 10, 5)
    assert item.calculate_total_price() == 50


def test_apply_discount():
    item = Item("Test item", 10, 5)
    item.apply_discount()
    assert item.price == 10 * item.__class__.pay_rate
