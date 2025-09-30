from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('create/', views.create_twet, name='create_twet'),
    path('<int:id>/', views.twet_detail, name='twet_detail'),
    path('<int:id>/edit/', views.edit_twet, name='edit_twet'),
    path('<int:id>/delete/', views.delete_twet, name='delete_twet'),
]
