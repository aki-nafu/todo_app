from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('uncomplete/<list_id>', views.uncomplete, name="uncomplete"),
    path('complete/<list_id>', views.complete, name="complete"),
    path('edit/<list_id>', views.edit, name="edit"),
]