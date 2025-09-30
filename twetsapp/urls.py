from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('create/', views.create_twet, name='create_twet'),
    path('<int:id>/', views.twet_detail, name='twet_detail'),
    path('<int:id>/edit/', views.edit_twet, name='edit_twet'),
    path('<int:id>/delete/', views.delete_twet, name='delete_twet'),
    path('twet/<int:id>/like/', views.like_twet, name="like_twet"),
    path('twet/<int:id>/comment/', views.add_comment, name="add_comment"),
    path("twet/<int:id>/", views.twet_detail, name="twet_detail"),
    path("comment/<int:id>/delete/", views.delete_comment, name="delete_comment"),
]
