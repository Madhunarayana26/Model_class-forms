from django.db import models
from django import forms

# Create your models here.
def check_for_name(name):
    if name[0].lower=='a' or len(name)<=5 :
        raise forms.ValidationError('conditions are not valid')


class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[check_for_name])
    url=models.URLField()
    def __str__(self) -> str:
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.author

