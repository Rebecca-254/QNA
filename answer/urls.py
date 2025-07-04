from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_id>/', views.question_detail, name='question-detail'), 
    path('', views.all_answers, name='all_answers')
]
