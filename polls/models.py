from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '%s ' % self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return '%s ' % self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '%s ' % self.choice_text
