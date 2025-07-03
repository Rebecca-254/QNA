from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_id>/', views.question_detail, name='question-detail'), 
]
