from django.http import HttpResponse
from django.shortcuts import render
from .models import Future
from django.contrib.auth.decorators import login_required
from .forms import FutureForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def futures(request):
    return render(request, 'futures.html', {
    	'futures': Future.objects.filter(user=request.user)
    })


def future(request):
    if request.method == 'POST':
        form = FutureForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = FutureForm()

    return render(request, 'future.html', {'form': form})