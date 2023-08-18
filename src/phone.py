from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
    def __add__(self, other):
        """
        Переопределение оператора сложения для экземпляров класса Phone и Item.

        :param other: Другой объект для сложения.
        :return: Общее количество товаров.
        :raises: ValueError, если количество физических SIM-карт не является целым числом больше нуля.
        """
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить Phone или Item с экземплярами других классов.")

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __repr__(self):
        """
        Возвращает строковое представление объекта Phone для отладки.
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        Возвращает строковое представление объекта Phone для вывода пользователю.
        """
        return self.name