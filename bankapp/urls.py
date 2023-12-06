from django.urls import path
from . import views

app_name = 'bankapp'

urlpatterns = [
    path('', views.next, name="next"),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('account_registration/', views.account_registration, name='account_registration'),
    path('member/', views.member, name='member'),
    path('next/', views.next, name="next"),
    path('next1', views.next1, name="next1"),
    path('get_branches/', views.get_branches, name='get_branches'),
    



]
