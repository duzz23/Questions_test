from django.urls import path, include
from .views import *
from question.views import *
from rest_framework import routers
from question.views import *


urlpatterns = [
    #страница регистрации пользователя
    path('', HomePage.as_view(), name='home'),

    path('register/', register, name='register'),
    path('login/', User_login, name='login'),
    path('logout/', User_logout, name='logout'),
    path('question1/', GetQuestion.as_view(), name='question1'),
    path('answer1/', QuestionAnswer.as_view(), name='answer1'),

]
