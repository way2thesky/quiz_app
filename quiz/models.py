from django.db import models


class Question(models.Model):
    question = models.CharField(unique=True, max_length=250)
    is_true = models.BooleanField(default=True)

    def __str__(self):
        return self.question
