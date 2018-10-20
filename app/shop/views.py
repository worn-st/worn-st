from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Future
from django.contrib.auth.decorators import login_required
from .forms import FutureForm, ChoiceForm


def index(request):
    return render(request, 'index.html', {
    })

@login_required
def futures(request):
    return render(request, 'futures.html', {
    	'futures': Future.objects.filter(user=request.user)
    })


@login_required
def show_future(request, pk):
    future =  Future.objects.get(id=pk)
    if request.method == 'POST':
        form = ChoiceForm(request.POST, request.FILES)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.user = request.user
            choice.future = future
            choice.save()

            return HttpResponseRedirect('/show_future/' + str(future.pk))
    else:
        form = ChoiceForm()

    return render(request, 'show_future.html', {
        'future':  Future.objects.get(id=pk),
        'form': form
    })


@login_required
def future(request):
    if request.method == 'POST':
        form = FutureForm(request.POST)
        if form.is_valid():
            future = form.save(commit=False)
            future.user = request.user
            future.save()

            return HttpResponseRedirect('/show_future/' + str(future.pk))
    else:
        form = FutureForm()

    return render(request, 'future.html', {'form': form})