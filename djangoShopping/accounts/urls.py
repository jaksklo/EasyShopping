from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/', LogoutView.as_view(),name= 'logout'),
    path('signup/', views.ESSignUp.as_view(), name='signup'),
    path('<int:pk>/', views.ESDetail.as_view(),name='userdetails'),
    path('edit/<int:pk>/', views.ESUpdateView.as_view(), name='useredit'),
    path('delete/<int:pk>/', views.ESDeleteView.as_view(), name='userdelete'),

]
