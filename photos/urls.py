from django.urls import path
from .views import PhotoListAPIView, PhotoDetailAPIView, CategoryListAPIView

urlpatterns = [
    path('photos/', PhotoListAPIView.as_view(), name='photo-list'), #PhotoListAPIView — это класс. Django ожидает функцию, а не класс. as_view() — это специальный метод класса, который превращает класс в функцию
    path('photos/<int:pk>/', PhotoDetailAPIView.as_view(), name='photo-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
]