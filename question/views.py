from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import Question

def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question-list')
    else:
        form = QuestionForm()
    return render(request, 'question/ask.html', {'form': form})

def question_list(request):
    questions = Question.objects.order_by('-created_at')
    return render(request, 'question/list.html', {'questions': questions})
