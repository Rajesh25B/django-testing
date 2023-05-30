from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from app1.models import Item


def homePage(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})
