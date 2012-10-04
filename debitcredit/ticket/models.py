from django.db import models
from member.models import Member
from django.forms import ModelForm

# Create your models here.

class Story_type(models.Model):
	story_type = models.CharField(max_length=200)

	def __unicode__(self):
		return self.story_type

class Story_state(models.Model):
	story_state = models.CharField(max_length=200)
	story_label = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s/%s" % (self.story_state,self.story_label)

class Label(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Ticket(models.Model):
	
	STORYPOINTS = (
		(0,0),
		(1,1),
		(2,2),
		(4,4),
		(8,8),
		)
	#(0,1,2,4,8,)

	title = models.CharField(max_length=2000)
	description = models.TextField()
	points = models.IntegerField(choices=STORYPOINTS)
	storytype = models.ForeignKey(Story_type)
	storystate = models.ForeignKey(Story_state)
	owner = models.ForeignKey(Member)
	requester = models.ForeignKey(Member,related_name='+')
	labels = models.ManyToManyField(Label)

	def __unicode__(self):
		return self.title

class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		
class LabelForm(ModelForm):
	class Meta:
		model = Label

class StoryStateForm(ModelForm):
	class Meta:
		model = Story_state

class StoryTypeForm(ModelForm):
	class Meta:
		model = Story_type
