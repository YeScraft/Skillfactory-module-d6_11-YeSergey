from django.db import models


# Create your models here.
class Author(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True,
    #                       verbose_name=_("Уникальный ключ"))
    full_name = models.CharField(max_length=256, verbose_name=("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=("Страна"))

    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Friend(models.Model):
    name = models.CharField(max_length=256, verbose_name="Имя друга")
    books = models.ManyToManyField('p_library.Book',
                                   through='Reading', verbose_name='Читает', related_name='books', blank=True)
                                   # through_fields=('friend', 'book'),
                                   # verbose_name='Читает')

    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    readers = models.ManyToManyField('p_library.Friend',
                                     through='Reading', verbose_name='Читатели', related_name='readers')
                                     # through_fields=('book', 'friend'),
                                     # verbose_name='Читатели')
    cover = models.ImageField(upload_to='book_covers', blank=True, verbose_name='Обложка книги')

    def __str__(self):
        return self.title

class Reading(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, verbose_name="Друг")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    # reader = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name="book_reader", )
    # status = models.NullBooleanField(default=None, verbose_name="Прочитано")

    def __str__(self):
        return "-".join((str(self.friend), str(self.book),))
                         # str(self.status),))


# Код из Вебинара

# class Friend(models.Model):
#     name = models.CharField(max_length=256, default='Имя', verbose_name="Имя друга")
#     books = models.ManyToManyField("p_library.Book", verbose_name="Книги",
#                                    through="p_library.BookReading",
#                                    through_fields=('friend', 'r_book', 'completion',))
#
#     def __str__(self):
#         return self.name
#
#
# class BookReading(models.Model):
#     friend = models.ForeignKey("p_library.Friend", on_delete=models.CASCADE,
#                                null=True,
#                                verbose_name="Читатель",
#                                related_name="friend")
#     r_book = models.ForeignKey("p_library.Book", on_delete=models.CASCADE,
#                              null=True,
#                              verbose_name="Книга",
#                              related_name="reading_book")
#     completion = models.NullBooleanField(default=None,
#                                          verbose_name="Прочитано")
#
#     def __str__(self):
#         return "-".join((str(self.r_book),
#                          str(self.friend),
#                          str(self.completion),))
