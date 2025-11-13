class Book:
    page_material = 'бумага'
    text_presence = True

    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def reserve(self):
        self.reserved = True

    def unreserve(self):
        self.reserved = False

    def print_info(self):
        reserved_text = ', зарезервирована' if self.reserved else ''
        print(
            f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
            f' материал: {self.page_material}{reserved_text}'
        )


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, reserved, subject, class_number, tasks):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.class_number = class_number
        self.tasks = tasks

    def print_info(self):
        reserved_text = ', зарезервирована' if self.reserved else ''
        print(
            f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
            f' предмет: {self.subject}, класс: {self.class_number}{reserved_text}'
        )


book1 = Book('Идиот', 'Достоевский', 500, '978-5-389-01746-7', False)
book2 = Book('Капитанская дочка', 'Пушкин', 160, '978-5-389-01746-8', False)
book3 = Book('Мастер и Маргарита', 'Булгаков', 400, '978-5-389-01746-9', False)
book4 = Book('Преступление и наказание', 'Достоевский', 590, '978-5-389-01747-9', False)
book5 = Book('Война и мир', 'Лев Толстой', 1225, '978-5-389-01741-9', False)

coursebook1 = SchoolBook('Алгебра', 'Иванов', 320, '978-5-389-02456-9', False, 'Математика', 9, True)
coursebook2 = SchoolBook('Геометрия', 'Иванов', 340, '978-5-389-02456-1', False, 'Математика', 8, False)
coursebook3 = SchoolBook('Родной язык', 'Сидорова', 388, '978-5-389-02456-2', False, 'Русский язык', 4, True)
coursebook4 = SchoolBook('История Руси', 'Артемов', 350, '978-5-389-02456-3', False, 'История', 5, False)
coursebook5 = SchoolBook('Всемирная история', 'Артемов', 322, '978-5-389-02456-4', False, 'История', 7, False)


book1.reserve()
book1.print_info()
book2.print_info()
book3.print_info()
book4.print_info()
book5.print_info()

coursebook1.reserve()
coursebook1.print_info()
coursebook2.print_info()
coursebook3.print_info()
coursebook4.print_info()
coursebook5.print_info()
