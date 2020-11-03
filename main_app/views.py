from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Finch, Toy
from .forms import FeedingForm, FinchForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Static
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# Finches
@login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user)

    return render(request, 'finches/index.html', { 'finches': finches })


@login_required
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    toys_finch_doesnt_have = Toy.objects.exclude(id__in=finch.toys.all().values_list('id'))

    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
    })


@login_required
def add_finch(request):
    if request.method == 'POST':
        finch_form = FinchForm(request.POST)
        if finch_form.is_valid():
            new_finch = finch_form.save(commit=False)
            new_finch.user = request.user
            new_finch.save()

            return redirect('detail', new_finch.id)
    else:
        form = FinchForm()
        context = { 'form': form }
        return render(request, 'finches/new.html', context)


# Finch Toys
@login_required
def assoc_toy(request, finch_id, toy_id):
    finch = Finch.objects.get(id=finch_id)
    toy = Toy.objects.get(id=toy_id)
    finch.toys.add(toy)
    return redirect('detail', finch_id= finch_id)


@login_required
def un_assoc_toy(request, finch_id, toy_id):
    finch = Finch.objects.get(id=finch_id)
    toy = Toy.objects.get(id=toy_id)
    finch.toys.remove(toy)
    return redirect('detail', finch_id= finch_id)


# Finch Feeding
@login_required
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


# Auth
def signup(request):
  error_message = ''

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
        error_message = 'Invalid sign up - try again'

        form = UserCreationForm()

        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)