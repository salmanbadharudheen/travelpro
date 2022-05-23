from django.http import HttpResponse
from django.shortcuts import render
from.models import place,dealer


# Create your views here.
def main(request):
    obj=place.objects.all()
    pers=dealer.objects.all()
    return render(request,"index.html",{'result':obj,'person':pers})