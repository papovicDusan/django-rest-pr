from django.urls import path, include
from todo_app.views import UserSetView, UserAuthView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('users/<int:pk>/', UserSetView.as_view(), name='user-detail'),
    path('api/users/me/', UserAuthView.as_view(), name='user-me'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
