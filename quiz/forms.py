from django.forms import ModelForm, TextInput, RadioSelect, Form, CharField, ChoiceField, forms
from .models import Question
from django import forms


class QuestForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question", "is_true"]
        choices = [('True', 'True'), ('False', 'False')]
        widgets = {
            "question": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter some long form content',
                'id': 'question',
                'rows': 3, 'cols': 80
            }),
            "is_true": RadioSelect(attrs={
                'id': 'correct_answer',
                'default': 'Unspecified'
            }, choices=choices, )
        }


class AnswerForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all(), required=True, widget=forms.HiddenInput)
    answer = forms.TypedChoiceField(choices=[(True, 'True'), (False, 'False')], widget=forms.RadioSelect,
                                    coerce=lambda x: x == 'True', )

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        if 'question' in self.initial:  # hack
            self.question_text = self.initial['question'].question

    def clean_question(self):
        data = self.cleaned_data['question']
        self.question_text = data.question  # hack
        return data
