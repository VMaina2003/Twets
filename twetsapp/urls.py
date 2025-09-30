from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("twetsapp.urls")),
    path('auth/', include("twetsauthenticationapp.urls")),
]
