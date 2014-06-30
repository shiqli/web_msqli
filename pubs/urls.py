from django.conf.urls import url, patterns
from pubs import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),
	url(r'^contact/thanks/$', views.thanks),
)
