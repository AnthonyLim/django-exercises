from ticket.models import Ticket,Story_state,Story_type,Label
from project.models import Project
from member.models import Member
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.
def create_story(request):
	form = TicketForm()
	#return HttpResponse(form)
	return render_to_response('new_input_form.html',
		{
		'form':form,
		},
		context_instance=RequestContext(request))

def save_story(request):
	form = TicketForm(request.POST)
	try:
		form.save()
		return render_to_response('blank.html',
		{
		'html':'<p>Story saved successfully.</p>',
		},
		context_instance=RequestContext(request))
	except ValueError as e:
		return HttpResponse(e)

def display_stories(request):
	tickets = Ticket.objects.all()
	types = Story_type.objects.all()
	states = Story_state.objects.all()

	return render_to_response('display_stories.html',
		{
		'tickets':tickets,
		'types':types,
		'states':states,
		},
		context_instance=RequestContext(request))