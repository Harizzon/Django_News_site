from django.urls import path, include
from .views import *


urlpatterns = [
       path('', index),
       path('articles/', articles),
       path('articles/<int:article_id>/', num_article),
       path('articles/archive/', archive),
       path('articles/archive/<int:article_id>/', num_archive),
       path('users/', users),
       path('users/<int:user_id>', num_users)


]