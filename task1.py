class Person:
    """
    Класс, описывающий человека в некоторой системе генерации текстовых диалогов.
    ...
    Атрибуты
    --------
    first_name : str
        имя персоны
    last_name : str
        фамилия персоны
    patronymic : str
        отчество персоны
    birth_date : str
        дата рождения персоны
    --------
    ...
    Методы
    ------
    __init__(self, first_name: str, last_name: str, patronymic: str, birth_date: str)
        Устанавливает все необходимые атрибуты для объекта Person.
    __repr__(self) -> str:
        Возвращает строку, при помощи которой можно создать экземпляр класса Person.
    __str__(self) -> str:
        Возвращает строковое отображение экземпляра класса для ознакомления с содержимым.
    dialog_speaker(self) -> str:
        Возвращает строку, используемую для указания авторства реплики при генерации диалога.
    say(self, replic: str) -> str:
        Возвращает строку реплики персоны при генерации диалога.
    ------
    """

    def __init__(self, first_name: str, last_name: str, patronymic: str, birth_date: str):
        """
        Устанавливает все необходимые атрибуты для объекта Person.

        Параметры
        ---------
            first_name : str
                имя персоны
            last_name : str
                фамилия персоны
            patronymic : str
                отчество персоны
            birth_date : str
                дата рождения персоны
        ---------
        """
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.birth_date = birth_date

    def __repr__(self) -> str:
        """
        Возвращает строку, при помощи которой можно создать экземпляр класса Person.
        Возвращаемое значение: str
        """
        return f"{self.__class__.__name__}(first_name={self.first_name!r}, last_name={self.last_name!r}," \
               f"patronymic={self.patronymic!r}, birth_date={self.birth_date!r})"

    def __str__(self) -> str:
        """
        Возвращает строковое отображение экземпляра класса для ознакомления с содержимым.
        Возвращаемое значение: str
        """
        if self.patronymic != "":
            return f"ФИО: {self.first_name} {self.last_name} {self.patronymic};\nДата рождения: {self.birth_date}."
        else:
            return f"ФИО: {self.first_name} {self.last_name};\nДата рождения: {self.birth_date}."

    def dialog_speaker(self) -> str:
        """
        Возвращает строку, используемую для указания авторства реплики при генерации диалога.
        Возвращаемое значение: str
        """
        return f"{self.first_name} {self.last_name} {self.patronymic}"

    def say(self, replic: str) -> str:
        """
        Возвращает строку реплики персоны при генерации диалога.

        Параметры
        ---------
            replic : str
                произносимая реплика
        ---------

        Возвращаемое значение: str
        """
        return f'{self.dialog_speaker()} говорит: "{replic}"'


class Student(Person):
    """
        Класс, описывающий студента в некоторой системе генерации текстовых диалогов.
        ...
        Атрибуты
        --------
        first_name : str
            имя студента
        last_name : str
            фамилия студента
        patronymic : str
            отчество студента
        birth_date : str
            дата рождения студента
        scores: dict{str: 2,3,4 или 5}
            Оценки студента по осваиваемым дисциплинам
        --------
        ...
        Методы
        ------
        Унаследованные:
        __init__(self, first_name, last_name, patronymic: str, birth_date: str, scores: dict)
            Устанавливает все необходимые атрибуты для объекта Student.
        __str__(self) -> str:
            Возвращает строковое отображение экземпляра класса для ознакомления с содержимым.
        say(self, replic: str) -> str:
            Возвращает строку реплики персоны при генерации диалога.
        ...
        Перегруженные:
        __repr__(self) -> str:
            Возвращает строку, при помощи которой можно создать экземпляр класса Student.
        dialog_speaker(self) -> str:
            Возвращает строку, используемую для указания авторства реплики при генерации диалога.
            Возвращаемое значение: str
        ...
        Новые:
        score_average(self) -> float:
            Вычисляет среднее арифметическое всех оценок по всем предметам.
        rank(self) -> str:
            Определяет место студента во внутривузовской иерархии.
        ------
    """
    def __init__(self, first_name, last_name, patronymic: str, birth_date: str, scores: dict):
        """
        Устанавливает все необходимые атрибуты для объекта Student.

        Параметры
        ---------
            first_name : str
                имя студента
            last_name : str
                фамилия студента
            patronymic : str
                отчество студента
            birth_date : str
                дата рождения студента
            scores: dict{str: 2,3,4 или 5}
                Оценки студента по осваиваемым дисциплинам
        ---------
        """

        super().__init__(first_name, last_name, patronymic, birth_date)
        self.scores = scores

    def __repr__(self) -> str:
        """
        Возвращает строку, при помощи которой можно создать экземпляр класса Person.
        Возвращаемое значение: str

        Перегрузка метода потребовалась по причине изменения конструктора дочернего класса относительно родительского.
        """
        return f"{self.__class__.__name__}(first_name={self.first_name!r}, last_name={self.last_name!r}, " \
               f"patronymic={self.patronymic!r}, birth_date={self.birth_date!r}, " \
               f"scores={self.scores!r})"

    @property
    def scores(self) -> dict:
        """Создание свойства потребовалось для вызова проверок каждый раз, когда делается попытка изменить self.scores"""
        return self._scores

    @scores.setter
    def scores(self, val: dict):
        if type(val) != dict:
            raise TypeError("Успеваемость студента зависывается в виде словаря с парой ключ-значение вида: str : 2,3,4 или 5")
        for subject in val:
            if not (val[subject] in [2, 3, 4, 5]):
                raise ValueError("Оценкой успеваемости студента по дисциплине могут быть числа 2, 3, 4 и 5")
        self._scores = val

    def score_average(self) -> float:
        """
        Вычисляет среднее арифметическое всех оценок по всем предметам.
        Возвращаемое значение: float
        """
        result = 0
        for subject in self.scores:
            result += self.scores[subject]
        return result / len(self.scores)

    def rank(self) -> str:
        """
        Определяет место студента во внутривузовской иерархии.
        Возвращаемое значение: str
        """
        grades = [0, 0, 0, 0]
        for subject in self.scores:
            grades[self.scores[subject] - 2] += 1

        if grades[0] + grades[1] + grades[2] == 0:
            return "Отличник"
        elif grades[0] + grades[1] == 0:
            return "Хорошист"
        elif grades[0] == 0:
            return "Троечник"
        else:
            return "Двоечник"

    def dialog_speaker(self) -> str:
        """
        Возвращает строку, используемую для указания авторства реплики при генерации диалога.
        Возвращаемое значение: str

        Перегрузка метода потребовалась, так как успеваемость студента значительно сказывается
        на степени доверия его словам.
        """
        return f"{super().dialog_speaker()} ({self.rank()})"

#Проверка работоспособности методов
if __name__ == "__main__":
    my_pers = Person("Иван", "Иванов", "Иванович", "07.07.2007")
    print(my_pers.say("Я отличник!"))
    my_stud = Student("Иван", "Иванов", "Иванович", "07.07.2007",
                        {"Матанализ": 5, "Теорвер": 4, "Философия": 3})
    print(my_stud.say("Я отличник!"))
