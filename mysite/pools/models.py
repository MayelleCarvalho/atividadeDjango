from django.db import models

# Create your models here.
class Question(models.Model):

    quest_text = models.CharField(max_length=255)
    closed = models.BooleanField()
    pub_date = models.DateField()

    def __str__(self):
        return self.quest_text


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name="choices", null=True)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text


