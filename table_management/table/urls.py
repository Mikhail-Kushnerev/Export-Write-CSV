from django.urls import path

from .views import export_csv

app_name = 'table'


urlpatterns = [
    path('', export_csv)
]
