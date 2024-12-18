import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):

        """
        Создание и подготовка к работе объекта "Книга"
        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)  # инициализация экземпляра класса
        """

        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def read_page(self, page_number: int) -> str:

        """
        Прочитать страницу книги.
        :param page_number: Номер страницы для чтения
        :return: Содержимое страницы
        :raise ValueError: Если номер страницы выходит за пределы книги
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_page(10)  # Вернет содержимое 10-й страницы
        'Содержимое страницы 10'
        """

        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть целым числом")
        if page_number < 1 or page_number > self.pages:
            raise ValueError("Номер страницы должен быть в пределах книги")
        return f"Содержимое страницы {page_number}"

    def get_total_pages(self) -> int:

        """
        Получить общее количество страниц в книге.
        :return: Количество страниц
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_total_pages()
        328
        """

        return self.pages

    def is_finished(self) -> bool:

        """
        Проверить, прочитана ли книга полностью.
        :return: True, если книга прочитана, иначе False
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.is_finished()
        False
        """

        return False  # По умолчанию книга не прочитана


class MusicalInstrument:
    def __init__(self, name: str, material: str, sound: str):

        """
        Создание и подготовка к работе объекта "Музыкальный инструмент"
        :param name: Название инструмента
        :param material: Материал, из которого изготовлен инструмент
        :param sound: Звук, издаваемый инструментом
        Примеры:
        >>> instrument = MusicalInstrument("Гитара", "Дерево", "Трунь")  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Название инструмента должно быть строкой")
        self.name = name

        if not isinstance(material, str):
            raise TypeError("Материал инструмента должен быть строкой")
        self.material = material

        if not isinstance(sound, str):
            raise TypeError("Звук инструмента должен быть строкой")
        self.sound = sound

    def play_sound(self) -> str:

        """
        Воспроизвести звук инструмента.
        :return: Звук инструмента
        Примеры:
        >>> instrument = MusicalInstrument("Гитара", "Дерево", "Трунь")
        >>> instrument.play_sound()
        'Трунь'
        """

        return self.sound

    def change_material(self, new_material: str) -> None:

        """
        Изменить материал инструмента.
        :param new_material: Новый материал инструмента
        Примеры:
        >>> instrument = MusicalInstrument("Гитара", "Дерево", "Трунь")
        >>> instrument.change_material("Пластик")
        """
        if not isinstance(new_material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = new_material

    def get_instrument_info(self) -> str:

        """
        Получить информацию об инструменте.
        :return: Информация об инструменте
        Примеры:
        >>> instrument = MusicalInstrument("Гитара", "Дерево", "Трунь")
        >>> instrument.get_instrument_info()
        'Гитара, Дерево, Трунь'
        """

        return f"{self.name}, {self.material}, {self.sound}"


class OperatingSystem:
    def __init__(self, name: str, version: str, is_multitasking: bool):

        """
        Создание и подготовка к работе объекта "Операционная система"
        :param name: Название операционной системы
        :param version: Версия операционной системы
        :param is_multitasking: Поддерживает ли система многозадачность
        Примеры:
        >>> os = OperatingSystem("Linux", "Ubuntu 20.04", True)  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Название ОС должно быть строкой")
        self.name = name

        if not isinstance(version, str):
            raise TypeError("Версия ОС должна быть строкой")
        self.version = version

        if not isinstance(is_multitasking, bool):
            raise TypeError("Многозадачность должна быть булевым значением")
        self.is_multitasking = is_multitasking

    def start_process(self, process_name: str) -> None:

        """
        Запустить процесс в операционной системе.
        :param process_name: Название процесса
        Примеры:
        >>> os = OperatingSystem("Linux", "Ubuntu 20.04", True)
        >>> os.start_process("Браузер")
        Запущен процесс: Браузер
        """

        if not isinstance(process_name, str):
            raise TypeError("Название процесса должно быть строкой")
        print(f"Запущен процесс: {process_name}")

    def get_os_info(self) -> str:

        """
        Получить информацию об операционной системе.
        :return: Информация об ОС
        Примеры:
        >>> os = OperatingSystem("Linux", "Ubuntu 20.04", True)
        >>> os.get_os_info()
        'Linux, Ubuntu 20.04, True'
        """

        return f"{self.name}, {self.version}, {self.is_multitasking}"

    def is_multitasking_supported(self) -> bool:

        """
        Проверить, поддерживает ли ОС многозадачность.
        :return: True, если поддерживает, иначе False
        Примеры:
        >>> os = OperatingSystem("Linux", "Ubuntu 20.04", True)
        >>> os.is_multitasking_supported()
        True
        """

        return self.is_multitasking

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации