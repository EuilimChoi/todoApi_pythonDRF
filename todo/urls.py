from django.urls import path
from .views import DoneTodoAPIView, TodoAPIView,TodoDetailAPIVIew

urlpatterns = [
    path('todo/', TodoAPIView.as_view()),
    path('todo/<int:pk>', TodoDetailAPIVIew.as_view()),
    path('done/',DoneTodoAPIView.as_view())
]