from django.contrib import admin
from django.urls import path
import main.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name='main'),
    path('result/', main.views.result, name='result')
]