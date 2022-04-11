from django.contrib import admin
from django.urls import path, re_path
from . import views


app_name = 'shoplists'

urlpatterns = [

    path('new/', views.ShoppingListCreateView.as_view(), name='createlist'),
    path('by/<str:username>/', views.UserShoppingLists.as_view(), name='listsbyuser'),
    path('by/<str:username>/<int:pk>/', views.ShoppingListDetailView.as_view(), name='details'),
    # path('<int:pk>/', views.ESDetail.as_view(),name='userdetails'),
    path('edit/<int:pk>/', views.ShoppingListUpdateView.as_view(), name='listedit'),
    path('delete/<int:pk>/', views.ShoppingListDeleteView.as_view(), name='listdelete'),

]
