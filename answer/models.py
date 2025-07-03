from django.db import models
from question.models import Question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    responder = models.CharField(max_length=100, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.responder} answered: {self.content[:30]}..."

