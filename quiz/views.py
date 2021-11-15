from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Question
from .forms import QuestForm, AnswerForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    return render(request, 'home.html')


def quiz(request):
    AnswerFormset = formset_factory(AnswerForm, max_num=3, min_num=3)
    if request.method == "GET":
        questions = Question.objects.order_by('?')[:3]
        formset = AnswerFormset(initial=[{'question': question} for question in questions])
    else:
        formset = AnswerFormset(request.POST)
        if formset.is_valid():
            correct, incorrect = 0, 0
            for data in formset.cleaned_data:
                if data['question'].is_true == data['answer']:
                    correct += 1
                else:
                    incorrect += 1
            return render(request, 'quiz/result.html', {'correct': correct, 'incorrect': incorrect})

    return render(request, 'quiz/list_quiz.html', {'formset': formset})


class QuizCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'quiz/create_quiz.html'
    form_class = QuestForm
    success_url = '/create_quiz'
    success_message = 'Question success added'
