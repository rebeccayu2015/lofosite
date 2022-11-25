from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def item_list(request):
    return render(request, 'main/item_list.html')

@login_required(login_url='/login/')
def add_item(request):
    return render(request, 'main/add_item.html')
