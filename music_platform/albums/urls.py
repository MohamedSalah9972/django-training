from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_album, name='create_albums'),
]