import doctest
class Table:
    def __init__(self, material: str, length: float, width: float):
        """
        Инициализация стола.

        :param material: Материал стола (например, дерево, металл).
        :param length: Длина стола в сантиметрах (должна быть больше 0).
        :param width: Ширина стола в сантиметрах (должна быть больше 0).
        :raises ValueError: Если length или width меньше или равен 0.
        """
        if length <= 0:
            raise ValueError("Длина должна быть больше 0.")
        if width <= 0:
            raise ValueError("Ширина должна быть больше 0.")

        self.material = material
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """
        Вычисляет площадь стола.

        :return: Площадь стола.
        :rtype: float
        :doctest:
        >>> table = Table("дерево", 200, 100)
        >>> table.calculate_area()
        20000
        """
        return self.length * self.width

    def describe(self) -> str:
        """
        Возвращает описание стола.

        :return: Описание стола.
        :rtype: str
        :doctest:
        >>> table = Table("металл", 150, 75)
        >>> table.describe()
        'Стол из металл размером 150x75 см.'
        """
        return f"Стол из {self.material} размером {self.length}x{self.width} см."

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации