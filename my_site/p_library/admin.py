from django.contrib import admin
# from .models import Book, Author, Publisher, Inspiration

# from django.db import models
# from django.forms import CheckboxSelectMultiple

from .models import Book, Author, Publisher
from .models import Friend, Reading

# from .models import Friend, BookReading
# from .models import Friend, Reader


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'publisher',)
    #
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }

    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publisher', 'price', 'copy_count', 'reader',)
    readonly_fields = ('readers',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    #@staticmethod
    #def author_full_name(obj):
        #return obj.full_name
    #list_display = ('author_full_name',) - так тоже работает

    list_display = ('full_name',)
    fields = ('full_name', 'birth_year', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)

# @admin.register(Inspiration)
# class InspirationAdmin(admin.ModelAdmin):
#     list_display = ('book', 'author', 'inspirer',)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('books',)

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('friend', 'book',)
    # list_display = ('friend', 'book', 'status',)
