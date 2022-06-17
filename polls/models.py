import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Question Model - has a question and a publication date.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)   # this causes future date to show as "recent" which is wrong
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    

# Choice Model - has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

"""
Migrations are very powerful and let you change your models over time, as you develop your project, 
without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, 
without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.

"""