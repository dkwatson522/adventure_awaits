from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Guide, Park
from .forms import GuideForm

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    guides = Guide.objects.filter(
        Q(parks__name__icontains=q) |
        Q(first_name__icontains=q) |
        Q(description__icontains=q)
        )
    parks = Park.objects.all()
    guide_count = guides.count

    context = {'guides': guides, 'parks': parks, 'guide_count': guide_count}
    return render(request, 'base/home.html', context)

def guide(request, pk):
    guide = Guide.objects.get(id=pk)

    context = {'guide': guide}
    return render(request, 'base/guide.html', context)

def createGuide(request):
    form = GuideForm()
    if request.method == 'POST':
        form = GuideForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/guide_form.html', context)

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

def deleteGuide(request, pk):
    guide = Guide.objects.get(id=pk)
    if request.method == 'POST':
        guide.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': guide})
