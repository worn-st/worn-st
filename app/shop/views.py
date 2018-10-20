from django.http import HttpResponse
from django.shortcuts import render
from .models import Future
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def futures(request):
    return render(request, 'futures.html', {
    	'futures': Future.objects.filter(user=request.user)
    })
