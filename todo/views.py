from django.shortcuts import render, redirect
from .models import Activities
# Create your views here.

def index(request):

    activity = Activities.objects.all()

    if request.method == 'POST':
        new_value = Activities(title=request.POST['title'])
        new_value.save()
        return redirect('/')

    return render(request, 'index.html', {'activity':activity})

def delete(request, pk):
    delete_item_id = Activities.objects.get(id=pk)
    delete_item_id.delete()
    return redirect('/')
