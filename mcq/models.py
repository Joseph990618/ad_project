from django.db import models

class Module(models.Model):
    module_name = models.CharField(max_length=10)

class Question(models.Model):
    module_under = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    question_under = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    choice_text1 = models.CharField(max_length=200, null=True)
    choice_text2 = models.CharField(max_length=200, null=True)
    choice_text3 = models.CharField(max_length=200, null=True)
    choice_text4 = models.CharField(max_length=200, null=True)
    answer_text = models.CharField(max_length=200, null=True)