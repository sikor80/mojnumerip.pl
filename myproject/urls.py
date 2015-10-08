from django.conf.urls import patterns, include, url
from django.http import HttpResponse

urlpatterns = patterns('',
	(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\n", mimetype="text/plain")),
    url(r'^$', 'mainapp.views.index'),
    url(r'^mapa', 'mainapp.views.mapa'),
    url(r'^kontakt', 'mainapp.views.kontakt'),
)
