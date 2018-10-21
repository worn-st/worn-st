from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Future, Choice
from django.contrib.auth.decorators import login_required
from .forms import FutureForm, ChoiceForm


def index(request):
    return render(request, 'index.html', {
    })

def shop(request):
    return render(request, 'shop.html', {
        'products': Choice.objects.filter(future__status='N')
    })

@login_required
def futures(request):
    return render(request, 'futures.html', {
    	'futures': Future.objects.filter(user=request.user)
    })


def purchases(request):
    return render(request, 'purchases.html', {
        'purchases': Future.objects.filter(buyer=request.user)
    })

def change_balance(user, delta):
    new = float(user.last_name) + float(delta)
    user.last_name = str(new)
    user.save()

def buy(request, pk):
    product = Choice.objects.get(id=pk)
    future = product.future
    future.status = 'D'
    future.buyer = request.user
    future.save()
    product.selected = True
    product.save()

    change_balance(request.user, -product.final_price())
    change_balance(future.user, product.final_price())

    return HttpResponseRedirect('/purchases')

def product(request, pk):
    product = Choice.objects.get(id=pk)
    return render(request, 'product.html', {
        'product': product,
        'form': ChoiceForm()
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