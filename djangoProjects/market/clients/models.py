from django.db import models

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    descriptions=models.CharField(max_length=300)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    Choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
class User(models.Model):
    user_name=models.CharField(max_length=500)
    email=models.CharField(max_length=100)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)

# Create your models here.
