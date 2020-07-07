from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('', include('auth_service.urls'))
]
