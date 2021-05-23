
from django.shortcuts import render

load=False
def index(request):
    return render(request,'base.html')
