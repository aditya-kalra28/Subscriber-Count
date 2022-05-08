from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def index(request):
    if request.method=='POST':
        channel=request.POST['channel']
        try:
            req = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?forUsername='+channel+'&key=AIzaSyBAiqtwaDhw4zWWrvp85MNPUch1JwHzZac&part=statistics')
            details=req.read()
            details_dict=json.loads(details)
            print(details_dict)
            data={
                'channel':channel,
                'subscriberCount':details_dict['items'][0]['statistics']['subscriberCount'],
                'viewCount':details_dict['items'][0]['statistics']['viewCount'],
                'videoCount':details_dict['items'][0]['statistics']['videoCount'],
                'error':False
            }
        except urllib.error.HTTPError as exception:
            data={
                'error':True
            }
    else:
        channel=''
        data={'channel':channel, 'error':False}
    return render(request,'index.html',data)
    # OR we can pass (request,'index.hmtl',{'city':city,'data':data})


