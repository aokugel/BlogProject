from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from .views import home
from blog.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('', home),
    path('blog/login/', login_view)
]

