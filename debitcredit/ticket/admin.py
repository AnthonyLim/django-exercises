from django.contrib import admin
from ticket.models import Ticket,Story_type,Story_state,Label

class TicketAdmin(admin.ModelAdmin):
	fields = ['title','storytype','points','storystate','requester','owner','description','labels']

admin.site.register(Ticket)
admin.site.register(Story_type)
admin.site.register(Story_state)
admin.site.register(Label)