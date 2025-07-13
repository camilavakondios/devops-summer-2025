from django.urls import re_path
from .views import book_view, health_view

app_name = 'api'




##here you add all the urls/endpoints that you want to expose
urlpatterns = [
    re_path(
        r"^$", health_view, name='health'
    ),
    re_path(
        r"^books/", book_view, name='books'
    )
    
    
]