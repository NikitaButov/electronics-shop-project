from src.item import Item

class LanguageMixin:
    """
    Миксин для хранения и изменения раскладки клавиатуры.
    """
    def init_language(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(LanguageMixin, Item):
    """
    Класс для представления товара "клавиатура".
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.init_language()

    def __str__(self):
        return self.name
