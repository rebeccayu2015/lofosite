from django.shortcuts import render

# Create your views here.
def item_list(request):
    return render(request, 'main/item_list.html')

def add_item(request):
    return render(request, 'main/add_item.html')