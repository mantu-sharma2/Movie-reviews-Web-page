from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='movie_list'),
    path('details/<int:id>/',views.details,name="details"),
    path('upvote/<int:id>/',views.upvote,name="upvote"),
]
