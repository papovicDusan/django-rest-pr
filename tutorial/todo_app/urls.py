from django.urls import path, include
from todo_app.views import UserSetView

urlpatterns = [
    path('users/<int:pk>/', UserSetView.as_view(), name='user-detail')
]
