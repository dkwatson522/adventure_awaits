from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Guide, Park
from .forms import GuideForm

def user_is_allowed(user):
    return user.is_superuser

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # sanitize username
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    guides = Guide.objects.filter(
        Q(parks__name__icontains=q) |
        Q(first_name__icontains=q) |
        Q(description__icontains=q)
        ).distinct()
    parks = Park.objects.all()
    guide_count = guides.count

    context = {'guides': guides, 'parks': parks, 'guide_count': guide_count}
    return render(request, 'base/home.html', context)

def guide(request, pk):
    guide = Guide.objects.get(id=pk)

    context = {'guide': guide}
    return render(request, 'base/guide.html', context)

@login_required(login_url='login')
@user_passes_test(user_is_allowed, login_url='error')
def createGuide(request):
    form = GuideForm()
    if request.method == 'POST':
        form = GuideForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/guide_form.html', context)

@login_required(login_url='login')
@user_passes_test(user_is_allowed, login_url='error')
def updateGuide(request, pk):
    guide = Guide.objects.get(id=pk)
    form = GuideForm(instance=guide)
    if request.method == 'POST':
        form = GuideForm(request.POST, instance=guide)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/guide_form.html', context)

@login_required(login_url='login')
@user_passes_test(user_is_allowed)
def deleteGuide(request, pk):
    guide = Guide.objects.get(id=pk)
    if request.method == 'POST':
        guide.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': guide})

def errorPage(request):
    messages.error(request, 'That page is restricted!')
    return redirect('home')
