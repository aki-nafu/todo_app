from todo_list.views import Create_account
from django.urls import path
from . import views
from django.contrib.auth.views import logout,login 

urlpatterns = [
    path('index', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('uncomplete/<list_id>', views.uncomplete, name="uncomplete"),
    path('complete/<list_id>', views.complete, name="complete"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('logout', logout, {'template_name': 'index.html'}, name='logout'), 
    path('', login, {'template_name': 'login.html'}, name='login'), 
    path('create_account', views.Create_account.as_view(), name='create_account'),
    path('accounts/profile/', views.profile, name="profile"), 
]


