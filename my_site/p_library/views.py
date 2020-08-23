from django.http import HttpResponse

from p_library.models import Book
from .forms import BookForm

from p_library.models import Publisher
from django.template import loader
from django.shortcuts import redirect, render

from .models import Author
from .forms import AuthorForm

from .models import Reading
from .forms import ReadingForm

from .models import Friend
from .forms import FriendForm

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

from django.http.response import HttpResponseRedirect

from django.forms import formset_factory
# AuthorFormSet = formset_factory(AuthorForm)

class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

class ReadingCreate(CreateView):
    model = Reading
    form_class = ReadingForm
    success_url = reverse_lazy('p_library:reading_list')
    template_name = 'reading_edit.html'

class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'reading_edit.html'

class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'

class ReadingList(ListView):
    model = Reading
    template_name = 'reading_list.html'

class FriendList(ListView):
    model = Friend
    template_name = 'friend_list.html'

class AuthorUpdate(UpdateView):
    model = Author
    fields = ["full_name", "birth_year", "country"]
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

class BookUpdate(UpdateView):
    model = Book
    fields = ['ISBN', 'title', 'description', 'year_release', 'copy_count', 'price', 'author', 'publisher', 'cover',]
    success_url = reverse_lazy('p_library:index')
    template_name = 'book_edit.html'

class ReadingUpdate(UpdateView):
    model = Reading
    fields = ['friend', 'book']
    success_url = reverse_lazy('p_library:reading_list')
    template_name = 'reading_edit.html'

class FriendUpdate(UpdateView):
    model = Friend
    fields = ['name', 'books']
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'reading_edit.html'

class AuthorDelete(DeleteView):
    model = Author
    form_class = AuthorForm
    fields = ["full_name", "birth_year", "country"]
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_delete.html'

class ReadingDelete(DeleteView):
    model = Reading
    form_class = ReadingForm
    # fields = ['friend', 'book']
    success_url = reverse_lazy('p_library:reading_list')
    template_name = 'reading_delete.html'

class FriendDelete(DeleteView):
    model = Friend
    fields = ['name', 'books']
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'reading_delete.html'

def books_list(request):
    # books = Book.objects.all()
    # return HttpResponse(books, request)
    return redirect('/index/')

# def index(request):
#     template = loader.get_template('index.html')
#     books = Book.objects.all()
#     biblio_data = {
#         "title": "мою библиотеку",
#         "books": books,
#     }
#     return HttpResponse(template.render(biblio_data, request))

class index(ListView):
    model = Book
    form_class = BookForm
    context_object_name = 'books'
    template_name = 'index.html'

def publisher(request):
    template = loader.get_template('publisher.html')
    publishers = Publisher.objects.all()
    publishers_data = {
        "publishers": publishers,
    }
    return HttpResponse(template.render(publishers_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

# AuthorFormSet = formset_factory(AuthorForm, extra=3)

# def author_create_many(request):
#     #  Первым делом, получим класс, который будет создавать наши формы.
#     #  Обратите внимание на параметр `extra`, в данном случае он равен 3, это значит,
#     #  что на странице с несколькими формами изначально будет появляться 3 формы создания авторов.
#     # AuthorFormSet = formset_factory(AuthorForm, extra=3)
#     #  Наш обработчик будет обрабатывать и GET и POST запросы.
#     #  POST запрос будет содержать в себе уже заполненные данные формы
#     if request.method == 'POST':
#         # Здесь мы заполняем формы формсета теми данными, которые пришли в запросе.
#         # Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм,
#         # но и разных формсетов, этот параметр позволяет их отличать в запросе.
#         author_formset = AuthorFormSet(request.POST, request.FILES, prefix='author')
#         #  Проверяем, валидны ли данные формы
#         if author_formset.is_valid():
#             for author_form in author_formset:
#                 #  Сохраним каждую форму в формсете
#                 author_form.save()
#             #  После чего, переадресуем браузер на список всех авторов.
#             return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
#         #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
#         else:
#             #  Инициализируем формсет и ниже передаём его в контекст шаблона.
#             author_formset = AuthorFormSet(prefix='author')
#         return render(request, 'manage_authors.html', {'author_formset': author_formset})

def is_save(author_form):
    try:
        author_form.save()
        return True
    except BaseException:
        return False

def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=3)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='author')
        if author_formset.is_valid():
            for author_form in author_formset:
                if is_save(author_form):
                    pass
                else:
                    return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='author')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})