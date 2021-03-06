from django.db import models
from django.contrib.auth.models import User

from os import remove
from random import choice

# Create your models here.

def gen_rand_str():
    res = ""
    alph = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(16):
        res += choice(alph)
    return res

def gen_rand_name(id, original_name):
    if original_name.endswith('.pdf'):
        return gen_rand_str() + '.pdf'
    return gen_rand_str() + '.docx'


class Case(models.Model):
    name = models.CharField(max_length=16, default=gen_rand_str)
    
    def __str__(self):
        return self.name


class String(models.Model):
    value = models.TextField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class Document(models.Model):
    file = models.FileField(upload_to=gen_rand_name)
    originalName = models.CharField(max_length=256)
    uid = models.CharField(max_length=16, default=gen_rand_str)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    isFinished = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        remove(file.name)
        super(Document, self).delete(*args, **kwargs)


class Rule(models.Model):
    name = models.CharField(max_length=100)
    # TODO: само правило
    
    def __str__(self):
        return self.name


"""
Все модели ниже оставлены на случай, если они понадобятся. В проекте на данный момент не используются
"""

class Profile(models.Model):
    name = models.CharField(max_length=100)
    rules = models.ManyToManyField(Rule)


class CaseType(models.Model):
    pass


#class Case(models.Model):
#    name = models.CharField(max_length=100)
#    caseType = models.ForeignKey(CaseType, on_delete=models.CASCADE)
    

class Report(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='document_to_check')
    templateDocument = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True, related_name='template')
    templateProfile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='template')
    #TODO: поле для содержимого отчёта
