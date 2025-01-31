
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user_data/<str:pk>/', get_user_profile_data),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_user),
    path('toggle_follow/', toggleFollow),
    path('posts/<str:pk/', get_users_posts),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
