from django.shortcuts import render
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# database models
from .models import tweets
# Create your views here.

def index(request):
   return render(request, 'index.html')

def tweet_data(request):
   if request.method == "POST":
      tweets_info = tweets(tweet = request.POST['tweet'],name = request.POST['name'])
      tweets_info.save()

   elif request.method == 'GET':
        tweeetData = serializers.serialize('json', tweets.objects.all())
        return HttpResponse(json.dumps(tweetData), content_type='application/json')