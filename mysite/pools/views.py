from django.shortcuts import render
from pools.models import Question, Choice
# Create your views here.


def index(request):

    questions = Question.objects.all()
    return render(request,
                  'index.html',
                  {'questions': questions})


def exibir_question(request, question_id):

    question = Question.objects.get(id = question_id)
    choices = Choice.objects.filter(question__id = question_id)
    return render(request,
                   'question.html',
                  {'question' : question,
                   'choices' : choices})