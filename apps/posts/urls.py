from django.urls import path

from apps.posts.views import add_post

app_name = 'posts'

urlpatterns = [
    path('add/', add_post, name='add_post')
]
