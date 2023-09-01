from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.comment_view, name='comment'),
    path('main/', views.main_view, name='main'),
]
