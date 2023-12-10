from typing import Union
import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Cat:
    """Класс, описывающий кота.
    ...
    Атрибуты
    --------
    name : str
        Имя кота

    weight : float
        Вес кота в Ньютонах

    length : float
        Длина кота в метрах

    Методы
    ------
    set_name(self, val: str):
        Выполняет проверку и запись значения имени.

    set_weight(self, val: float):
        Выполняет проверку и запись значения веса.

    set_length(self, val: float):
        Выполняет проверку и запись значения длины.

    __init__(self, name, weight, length):
        Устанавливает все необходимые атрибуты для объекта Cat.
        Параметры
        ---------
        name : str
                Имя кота
        weight : str
                Вес кота в Нютонах
        length : int
                Длина кота в метрах

    purr(self):
        Выводит мурчание кота.

    info(self):
        Выводит информацию о коте.
    """

    name = None     # Имя кота
    weight = None   # Вес кота в Ньютонах
    length = None   # Длина кота в метрах

    def set_name(self, val: str):
        """Выполняет проверку и запись значения имени."""
        if type(val) != str:
            raise TypeError("Кличка кота должна быть строкой!")
        if any(c.isdigit() for c in val):
            raise ValueError("Кличка кота не может содержать цифры!")
        self.name = val

    def set_weight(self, val: Union[float, int]):
        """Выполняет проверку и запись значения веса."""
        if not (isinstance(val, Union[float, int])):
            raise TypeError("Вес кота должен иметь тип float!")
        if val <= 0:
            raise ValueError("Вес кота - положительное число!")
        self.weight = val

    def set_length(self, val: Union[float, int]):
        """Выполняет проверку и запись значения длины."""
        if not (isinstance(val, Union[float, int])):
            raise TypeError("Длина кота должна иметь тип float!")
        if val <= 0:
            raise ValueError("Длина кота - положительное число!")
        self.length = val

    def purr(self):
        """Выводит мурчание кота."""
        print(f"{self.name}: *Мурчит*")

    def info(self):
        """Выводит информацию о коте."""
        print("Информация о коте:")
        print(f"Имя: {self.name}")
        print(f"Вес: {self.weight} Н")
        print(f"Длина: {self.length} м")

    def __init__(self, name, weight, length):
        """
        Устанавливает все необходимые атрибуты для объекта Cat.
        Параметры
        ---------
        name : str
                Имя кота
        weight : str
                Вес кота в Нютонах
        length : int
                Длина кота в метрах
        """
        self.set_name(name)
        self.set_weight(weight)
        self.set_length(length)


class Hotel:
    """Класс, описывающий отель в неком сервисе по подбору отелей.
    ...
    Атрибуты
    --------
    cost : float
        Стоимость в рублях проживания в отеле в течение суток

    rating : float
        Рейтинг отеля на сервисе от 0 до 5

    votes : int
        Число людей, оценивших отель на сервисе


    Методы
    ------
    set_cost(self, val: Union[float, int]):
        Выполняет проверку и запись значения стоимости проживания в отеле.

    set_votes(self, val: int):
        Выполняет проверку и запись значения числа оценивших отель.

    set_rating(self, val: Union[float, int]):
        Выполняет проверку и запись значения рейтинга отеля.

    __init__(self, cost, rating, votes):
        Устанавливает все необходимые атрибуты для объекта Hotel.
        Параметры
        ---------
        cost : float
            Стоимость в рублях проживания в отеле в течение суток
        rating : float
            Рейтинг отеля на сервисе от 0 до 5
        votes : int
            Число людей, оценивших отель на сервисе

    cost_living(self, days: int):
        Возвращает стоимость проживания в отеле в течение days суток.

    vote(self, rating: int):
        Позволяет оценить отдель, изменив тем самым общий рейтинг.

    info(self):
        Выводит информацию об отеле.
    """
    cost = None     # Стоимость в рублях проживания в отеле в течение суток
    rating = None   # Рейтинг отеля на сервисе от 0 до 5
    votes = None    # Число людей, оценивших отель на сервисе

    def set_cost(self, val: Union[float, int]):
        """Выполняет проверку и запись значения стоимости проживания в отеле."""
        if not (isinstance(val, Union[float, int])):
            raise TypeError("Стоимость проживания в отеле должна быть действительным числом!")
        if val <= 0:
            raise ValueError("Стоимость проживания в отеле - положительное число!")
        self.cost = val

    def set_votes(self, val: int):
        """Выполняет проверку и запись значения числа оценивших отель."""
        if type(val) != int:
            raise TypeError("Количество оценок должно быть неотрицательным целым числом!")
        if val < 0:
            raise ValueError("Количество оценок должно быть неотрицательным целым числом!")
        self.votes = val

    def set_rating(self, val: Union[float, int]):
        """Выполняет проверку и запись значения рейтинга отеля."""
        if not (isinstance(val, Union[float, int])):
            raise TypeError("Рейтинг отеля является целым или дробным числом от 0 до 5!")
        if val <= 0:
            raise ValueError("Рейтинг отеля не может быть отрицательным!")
        if val > 5:
            raise ValueError("Рейтинг отеля не может быть больше 5!")
        self.rating = val

    def __init__(self, cost, rating, votes):
        """
        Устанавливает все необходимые атрибуты для объекта Hotel.
        Параметры
        ---------
        cost : float
            Стоимость в рублях проживания в отеле в течение суток
        rating : float
            Рейтинг отеля на сервисе от 0 до 5
        votes : int
            Число людей, оценивших отель на сервисе
        """
        self.set_cost(cost)
        self.set_rating(rating)
        self.set_votes(votes)

    def cost_living(self, days: int):
        """
        Возвращает стоимость проживания в отеле в течение days суток.

        days: int
            Количество дней проживания в отеле

        return: float

        Пример
        ------
        >>> my_hotel = Hotel(5, 1, 2)
        >>> my_hotel.cost_living(4)
        20.0
        """

        if type(days) != int:
            raise TypeError("Количество суток должно быть натуральным числом!")
        if days <= 0:
            raise ValueError("Количество суток должно быть натуральным числом!")
        return float(days * self.cost)

    def vote(self, rating: int):
        """
        Позволяет оценить отель на rating, изменив тем самым общий рейтинг.

        rating: int
            Оценка, выставляемая пользователем. Натуральное число от 0 до 5"""
        if type(rating) != int:
            raise TypeError("Рейтинг отедля должен быть натуральным числом!")
        if rating < 0:
            raise ValueError("Рейтинг отеля не может быть отрицательным!")
        if rating > 5:
            raise ValueError("Рейтинг отеля не может быть больше 5!")
        self.votes += 1
        self.rating = (self.rating * (self.votes - 1) + rating) / self.votes

    def info(self):
        """Выводит информацию об отеле"""
        print("Информация об отеле:")
        print(f"Стоимость проживания: {self.cost} руб./сут.")
        print(f"Рейтинг отеля: {self.rating} из 5")
        print(f"Число проголосовавших: {self.votes}")


class Car:
    """Класс, описывающий автомобиль с точки зрения логистической задачки.
    ...
    Атрибуты
    --------
    speed : float
        Максимальная скорость перемещения автомобиля в метрах в секунду

    fuel : float
        Текущее количество топлива в автомобиле в литрах

    fuel_limit : int
        Максимальное количество топлива автомобиля в литрах


    Методы
    ------
    set_speed(self, val: Union[float, int]):
        Выполняет проверку и запись значения скорости автомобиля.

    set_fuel(self, val: Union[float, int]):
        Выполняет проверку и запись значения количества топлива автомобиля.

    set_fuel_limit(self, val: Union[float, int]):
        Выполняет проверку и запись значения максимального количества топлива автомобиля.

    __init__(self, speed, fuel, fuel_limit):
        Устанавливает все необходимые атрибуты для объекта Car.
        Параметры
        ---------
        speed : float
            Максимальная скорость перемещения автомобиля в метрах в секунду
        fuel : float
            Текущее количество топлива в автомобиле в литрах
        fuel_limit : int
            Максимальное количество топлива автомобиля в литрах

    recharge(self, val: Union[float, int]):
        Заправка автомобиля на количество топлива val

    info(self):
        Выводит информацию об автомобиле
    """
    speed = None        # Максимальная скорость перемещения автомобиля в метрах в секунду
    fuel = None         # Текущее количество топлива в автомобиле в литрах
    fuel_limit = None   # Максимальное количество топлива автомобиля в литрах

    def set_speed(self, val: Union[float, int]):
        """Выполняет проверку и запись значения скорости автомобиля."""
        if not (isinstance(val, Union[float, int])):
            raise TypeError("Скорость автомобиля должна быть действительным числом!")
        if val <= 0:
            raise ValueError("Скорость автомобиля - положительное число!")
        self.speed = val

    def set_fuel(self, val: Union[float, int]):
        """Выполняет проверку и запись значения количества топлива автомобиля."""
        if not (isinstance(val, Union[float, int])):
            raise TypeError("Количество топлива автомобиля должно быть действительным числом!")
        if val <= 0:
            raise ValueError("Количество топлива автомобиля - положительное число!")
        if val > self.fuel_limit:
            val = self.fuel_limit
        self.fuel = val

    def set_fuel_limit(self, val: Union[float, int]):
        """Выполняет проверку и запись значения максимального количества топлива автомобиля."""
        if not (isinstance(val, Union[float, int])):
            raise TypeError("Максимальное количество топлива автомобиля должно быть действительным числом!")
        if val <= 0:
            raise ValueError("Максимальное количество топлива автомобиля - положительное число!")
        self.fuel_limit = val

    def __init__(self, speed, fuel, fuel_limit):
        """
        Устанавливает все необходимые атрибуты для объекта Car.
        Параметры
        ---------
        speed : float
            Максимальная скорость перемещения автомобиля в метрах в секунду
        fuel : float
            Текущее количество топлива в автомобиле в литрах
        fuel_limit : int
            Максимальное количество топлива автомобиля в литрах
        """
        self.set_speed(speed)
        self.set_fuel_limit(fuel_limit)
        self.set_fuel(fuel)

    def recharge(self, fuel: Union[float, int]):
        """
        Заправка автомобиля на количество топлива fuel

        fuel: int, float
            Количество заливаемого в автомобиль топлива"""
        if not (isinstance(fuel, Union[float, int])):
            raise TypeError("Количество заправляемого топлива автомобиля должно быть действительным числом!")
        if fuel <= 0:
            raise ValueError("Количество заправляемого топлива автомобиля - положительное число!")
        self.set_fuel(self.fuel + fuel)

    def info(self):
        """Выводит информацию об автомобиле"""
        print("Информация об автомобиле:")
        print(f"Максимальная скорость: {self.speed} м/с")
        print(f"Запас топлива: {self.fuel} л из {self.fuel_limit} л")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
