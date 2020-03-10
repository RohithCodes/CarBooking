from django.urls import path
from .views import Book_Details

urlpatterns=[
    path(r'getdata', Book_Details.as_view()),
]