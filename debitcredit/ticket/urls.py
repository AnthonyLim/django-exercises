from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('',
	url(r'^$','ticket.views.display_stories'),
	url(r'^new/$','ticket.views.create_story'),
	url(r'^save$','ticket.views.save_story'),
)
