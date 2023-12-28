from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    return HttpResponse('Hello!')


def item_views(request):
    items = Item.objects.all()
    context = {'item': items}
    return render(request, 'west_api/item_views.html', context)
