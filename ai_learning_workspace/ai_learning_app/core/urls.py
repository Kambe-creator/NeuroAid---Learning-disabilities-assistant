from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('customize-avatar/', views.customize_avatar, name='customize_avatar'),
    path('avatar-success/', views.avatar_success, name='avatar_success'),
    path('chatbot/', views.chatbot, name='chatbot'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customize-avatar/', views.customize_avatar, name='customize_avatar'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
