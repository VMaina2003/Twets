from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),       # Home/Feed
    path('create/', views.create_twet, name='create_twet'),  # Post new tweet
    path('<int:id>/', views.twet_detail, name='twet_detail'),  # View single tweet
]
