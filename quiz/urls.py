from django.conf.urls import url
from django.urls import path

from .views import QuizCreateView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('create_quiz/', QuizCreateView.as_view(), name='create_quiz'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
