
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import CreateShortURL

urlpatterns = [
    path('admin/', admin.site.urls),
    path("<str:url>", views.redirect),
    path("", views.home),
    path('create/',CreateShortURL , name = 'create')
]

