from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:slot_id>', views.show_data, name='show_data'), 
]
