from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show_articles, name='index'),
    path('create', views.create_article, name='article_creation'),
    path('article/<int:article_id>/', include([
        path('', views.get_article, name='article'),
        path('update', views.update_article, name='article_update'),
        path('delete', views.delete_article, name='article_delete'),
    ])),
]
