from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_articles, name='index'),
    path('article/<int:id>', views.article_view, name='article'),
]
