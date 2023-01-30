from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name = 'index'),
    path('result', views.result),
    path('polling_unit', views.polling_unit)
]