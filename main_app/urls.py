from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Static
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Finches
    path('finches/', views.finches_index, name='index'),
    path('finches/new/', views.add_finch, name='add_finch'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/<int:finch_id>/delete', views.delete_finch, name='delete_finch'),
    path('finches/<int:finch_id>/edit', views.edit_finch, name='edit_finch'),
    # Finch Feeding
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # Finch Toys
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('finches/<int:finch_id>/un_assoc_toy/<int:toy_id>/', views.un_assoc_toy, name='un_assoc_toy'),
    # Auth
    path('accounts/signup', views.signup, name='signup'),
]