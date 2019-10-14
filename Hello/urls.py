from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('add_new/', views.add_new, name='add_new'),
    path('edit/<id>/', views.edit, name='edit'),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<id>/', views.update, name='update'),

]