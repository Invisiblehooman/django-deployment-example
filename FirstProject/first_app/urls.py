from django.urls import path
from .views import index, help, form_view

urlpatterns = [
    path('', index, name='index'),
    path('help/', help, name='help'),
    path('user/', form_view, name='form' )
]