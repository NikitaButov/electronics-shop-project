import pytest
from src.keyboard import Keyboard


def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5


def test_keyboard_str_representation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == 'Dark Project KD87A'


def test_keyboard_default_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'


def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    # Initial language should be 'EN'
    assert kb.language == 'EN'

    # Change language to 'RU'
    kb.change_lang()
    assert kb.language == 'RU'

    # Change language back to 'EN'
    kb.change_lang()
    assert kb.language == 'EN'


def test_keyboard_change_language_chain():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    # Initial language should be 'EN'
    assert kb.language == 'EN'

    # Chain method calls to change language: EN -> RU -> EN -> RU
    kb.change_lang().change_lang().change_lang()
    assert kb.language == 'RU'


def test_keyboard_set_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    # Set language to 'FR'
    kb.language = 'FR'
    assert kb.language == 'FR'