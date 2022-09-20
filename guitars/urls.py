from django.urls import path
from . import views

urlpatterns = [
    path('guitars/', views.GuitarsPage.as_view(), name='guitars'),
    path('submitguitar/', views.submit_guitar, name='submit-guitar'),
    path('<slug:slug>/', views.GuitarsPagePost.as_view(), name='guitars-post'),
    path('like/<slug:slug>', views.LikeGuitarPost.as_view(), name='like-guitars'),
]