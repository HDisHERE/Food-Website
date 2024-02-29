from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ourgoal/', views.ourgoal, name='ourgoal'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
]