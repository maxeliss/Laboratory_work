import doctest
from typing import Union

class Card:
    def __init__(self, owner: str, balance: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Карта"

        :param owner: Фамилия и имя владельца карты
        :param balance: Баланс карты в рублях

        Примеры:
        >>> card = Card("IVANOV IVAN", 10000)
        """
        self.owner = owner
        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс карты должен быть типа int или float")
        self.balance = balance

    def deposit(self, deposit: Union[int, float]) -> None:
        """
        Функция которая показывает баланс после зачисления денег
        :param deposit: Зачисленные деньги

        :raise ValueError: Если зачисленные деньги отрицательное число, то выдает ошибку

        Примеры:
        >>> card = Card("IVANOV IVAN", 5000)
        >>> card.deposit(3000)
        """
        if not isinstance(deposit, (int, float)):
            raise TypeError("Зачисленные деньги должны быть типа int или float")
        if deposit <= 0:
            raise ValueError("Зачисленные деньги не могут быть отрицательным числом")

    def withdraw(self, withdraw: Union[int, float]) -> None:
        """
        Функция которая показывает баланс после снятия денег
        :param withdraw: Снятые деньги

        :raise ValueError: Если снятые деньги отрицательное число, то выдает ошибку
        :raise ValueError: Если снятые деньги больше баланса, то выдает ошибку
        Примеры:
        >>> card = Card("IVANOV IVAN", 5000)
        >>> card.withdraw(5000)
        """
        if not isinstance(withdraw, (int, float)):
            raise TypeError("Снятые деньги должны быть типа int или float")
        if withdraw <= 0:
            raise ValueError("Снятые деньги не могут быть отрицательным числом")
        if withdraw > self.balance:
            raise ValueError("Снятые деньги не могут быть больше баланса")


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации