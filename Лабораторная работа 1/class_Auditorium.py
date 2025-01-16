import doctest


class Auditorium:
    def __init__(self, number_of_seats: int, number_of_people: int):
        """
        Создание и подготовка к работе объекта "Скамейка"

        :param number_of_seats: Количество сидячих мест
        :param number_of_people: Количество сидящих людей

        Примеры:
        >>> auditorium = Auditorium(100, 20)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_seats, int):
            raise TypeError("Количество сидясих мест должно быть типа int")
        if number_of_seats <= 0:
            raise ValueError("Количество сидячих мест должно быть положительным числом")
        self.number_of_seats = number_of_seats

        if not isinstance(number_of_people, int):
            raise TypeError("Количество сидящих людей должно быть int")
        if number_of_people < 0:
            raise ValueError("Количество сидящих людей не может быть отрицательным числом")
        self.number_of_people = number_of_people

    def is_empty_auditorium(self) -> bool:
        """
        Функция которая проверяет является ли аудитория пустой

        :return: Является ли аудитория пустой

        Примеры:
        >>> auditorium = Auditorium(150, 0)
        >>> auditorium.is_empty_auditorium()
        """
        ...

    def new_people(self, new_people: int) -> None:
        """
        Счет количества людей в аудитории после тоого, как зашли новые
        :param new_people: Колличество новых севших людей

        :raise ValueError: Если количество новых севших людей превышает свободные места в аудитории, то вызываем ошибку

        Примеры:
        >>> auditorium = Auditorium(100, 20)
        >>> auditorium.new_people(80)
        """
        if not isinstance(new_people, int):
            raise TypeError("Колличество новых севших людей должно быть типа int")
        if new_people < 0:
            raise ValueError("Колличество новых севших людей не должно быть отрицательным")
        if new_people > (self.number_of_seats - self.number_of_people):
            raise ValueError( "Количество новых людей не должно превышать количество свободных мест")

    def departed_people(self, departed_people: int) -> None:
        """
        Счет количества людей в аудитории после того, как ушла часть людей

        :param departed_people: Количество ушедших людей
        :raise ValueError: Если количество ушедших людей превышает количество сидящих людей, то возвращается ошибка.

        :return: Количество ушедших людей

        Примеры:
        >>> auditorium = Auditorium(100, 90)
        >>> auditorium.departed_people(20)
        """
        if not isinstance(departed_people, int):
            raise TypeError("Колличество ушедших людей должно быть типа int")
        if departed_people < 0:
            raise ValueError("Колличество ушедших людей не должно быть отрицательным")
        if departed_people > self.number_of_people
            raise ValueError("Количество ушедших людей не может превышать количество сидящих людей")


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации