from django.shortcuts import render
import feedparser


def index(request):
 
    if request.GET.get('url'):
 
        url = request.GET['url'] # Getting URL
 
        feed = feedparser.parse(url) # Parsing XML data
 
    else:
        feed = None
 
    return render(request, 'rss/reader.html', {
 
        'feed': feed,

    })
