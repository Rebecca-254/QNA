from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question-list'),
    path('ask/', views.ask_question, name='ask-question'),  
]
