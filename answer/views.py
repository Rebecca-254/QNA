from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnswerForm
from .models import Answer
from question.models import Question

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question-detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'answer/detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })
