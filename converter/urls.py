from django.urls import path
from converter.views import convert_currency

urlpatterns = [
    path('', convert_currency, name='convert_currency'),
]
