from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('<int:num>/', views.index, name='index'),
    path('', views.index, name='index')
]
