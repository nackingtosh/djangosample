from django.db import models

# Create your models here.

class Question(models.Model):
	def __str__(self):
		return self.question_text
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	def __str__(self):
		return self.choice.text
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
