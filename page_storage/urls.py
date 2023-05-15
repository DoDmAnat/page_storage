from django.urls import path
from .views import PageListAPIView, PageDetailAPIView

urlpatterns = [
    path('pages/', PageListAPIView.as_view(), name='page-list'),
    path('pages/<slug:slug>/', PageDetailAPIView.as_view(), name='page-detail'),
]
