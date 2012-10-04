from django.db import models
from django.forms import ModelForm

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=2000)
	initials = models.CharField(max_length=2)

	def __unicode__(self):
		return self.name

class MemberForm(ModelForm):
	class Meta:
		model = Member