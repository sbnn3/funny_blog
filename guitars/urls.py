from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.GuitarsPage.as_view(), name='music'),
]