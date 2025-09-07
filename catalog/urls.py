from django.urls import path
from .views import home_page, contacts_page

urlpatterns = [
    path('', home_page, name='home'),
    path('contacts/', contacts_page, name='contacts'),
]