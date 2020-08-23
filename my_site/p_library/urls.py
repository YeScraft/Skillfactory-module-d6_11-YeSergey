from django.contrib import admin
from django.urls import path
from .views import AuthorCreate, AuthorList, author_create_many, AuthorDelete, AuthorUpdate
from .views import ReadingList, ReadingUpdate, ReadingCreate, ReadingDelete
from .views import FriendList, FriendUpdate, FriendDelete, FriendCreate
from .views import BookUpdate, index

app_name = 'p_library'

urlpatterns = [
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/create_many/', author_create_many, name='author_create_many'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author_edit'),
    path('reading/create/', ReadingCreate.as_view(), name='reading_edit'),
    path('reading/', ReadingList.as_view(), name='reading_list'),
    path('reading/<int:pk>/', ReadingUpdate.as_view(), name='reading_edit'),
    path('reading/<int:pk>/delete/', ReadingDelete.as_view(), name='reading_delete'),
    path('friend/create/', FriendCreate.as_view(), name='friend_create'),
    path('friend/', FriendList.as_view(), name='friend_list'),
    path('friend/<int:pk>/', FriendUpdate.as_view(), name='friend_edit'),
    path('friend/<int:pk>/delete/', FriendDelete.as_view(), name='friend_delete'),
    path('index/<int:pk>/', BookUpdate.as_view(), name='book_edit'),
    path('index/', index.as_view(), name='index'),
]
