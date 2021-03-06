from django.shortcuts import render, redirect
from pools.models import Question, Choice
# Create your views here.


def index(request):

    questions = Question.objects.order_by('-pub_date').all()
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


def exibir_manage(request, question_id):

    questions = Question.objects.all()

def remove(request, question_id, question):
    question_a_remover = Question.objects.get(id=question_id)

	question.remover(question_a_remover)
    return redirect('index')




