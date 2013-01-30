# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

import feedparser
def index(request):
	alt1040 = feedparser.parse('http://alt1040.com/feed')
	# x = alt1040.entries[1].title
	# x = x.encode('UTF-8')
	# print x
	latest_poll_list = alt1040.entries


	wwwhat = feedparser.parse('http://wwwhatsnew.com/feed/')
	# x = alt1040.entries[1].title
	# x = x.encode('UTF-8')
	# print x
	latest_poll_list2 = wwwhat.entries
	title =  wwwhat.feed.title
	template = loader.get_template('index.html')
	context = Context({
		'latest_poll_list': latest_poll_list,
	    'latest_poll_list2': latest_poll_list2,
	    'title_2': title
	})


	return HttpResponse(template.render(context))


