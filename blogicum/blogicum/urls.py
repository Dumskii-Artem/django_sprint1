from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index/', include('blog.urls', namespace='blog')),
    path('posts/', include('blog.urls', namespace='blog')),
    path('category/', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog'))
]
