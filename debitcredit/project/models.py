from django.db import models
from member.models import Member
from django.forms import ModelForm

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=200)
	details = models.TextField()
	createdon = models.DateTimeField('Date Created',auto_now=True)
	createdby = models.ForeignKey(Member)

	def __unicode__(self):
		return self.name

class ProjectForm(ModelForm):
	class Meta:
		model = Project