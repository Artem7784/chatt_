from django.urls import path
from .views import index, get_messages, post_message

urlpatterns = [
    path('', index, name='index'),
    path('get_messages/', get_messages, name='get_messages'),
    path('post_message/', post_message, name='post_message'),
]
