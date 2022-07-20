from django.urls import path, include
from .views import *
from question.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'question', GetQuestion)

urlpatterns = [
    #страница регистрации пользователя
    path('', HomePage.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', User_login, name='login'),
    path('logout/', User_logout, name='logout'),
    path('question/', GetQuestion.as_view(), name='question'),
    path('answer/', QuestionAnswer.as_view(), name='answer'),

    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
