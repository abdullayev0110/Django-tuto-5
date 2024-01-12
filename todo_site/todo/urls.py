from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='todo'),
    path('del/<str:item_id>', views.remove, name='del'),
]
