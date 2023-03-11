from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from main.models import Item
from datetime import datetime
from django.utils import timezone
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login/')
def item_list(request):
    items = Item.objects.filter(status="Claimed") | Item.objects.filter(status="Unclaimed")

    # item = Item(item_name="Sample Item",
    #             curr_user=request.user,
    #             where_found="Cafeteria",
    #             where_left="Front Office",
    #             description="Sample description",
    #             status='Unclaimed')
    # item.save()

    # "Delete" after 15 seconds (practically 1 day)
    for item in Item.objects.filter(status="Claimed"):
        duration = timezone.now() - item.time_claimed
        duration_in_s = duration.total_seconds()

        if duration_in_s > 30:
            item.status = "Verified"
            item.save()

    # Claim and unclaim logic
    if request.method == "POST":
        id = request.POST.get('item-id')
        item = Item.objects.filter(item_id=id).first()
        
        if item.status == "Unclaimed" and item.curr_user == request.user:
            item.delete()
            messages.warning(request, "Deleted item \"" + item.item_name + "\".")
            return redirect('item_list')
        elif item.status == "Unclaimed":
            item.claim_user = request.user
            item.time_claimed = datetime.now()
            item.status = "Claimed"
            item.save()
            messages.success(request, "Claimed item \"" + item.item_name + "\".")
            return redirect('item_list')
        elif item.status == "Claimed":
            item.claim_user = None
            item.time_claimed = None
            item.status = "Unclaimed"
            item.save()
            messages.warning(request, "Unclaimed item \"" + item.item_name + "\".")
            return redirect('item_list')

    user = request.user
    context = {
        'items': items,
        'user': user
    }

    return render(request, 'main/item_list.html', context)

@login_required(login_url='/login/')
def add_item(request):
    # Add item to database (add image functions)
    if request.method == 'POST':
        name = request.POST['item-name']
        location_found = request.POST['location-found']
        location_left = request.POST['location-left']
        item_descrip = request.POST['item-descrip']
        item_image = request.FILES['item-image']

        item = Item(item_name=name,
                    curr_user=request.user,
                    where_found=location_found,
                    where_left=location_left,
                    description=item_descrip,
                    image=item_image,
                    status='Unclaimed')
        item.save()
        messages.success(request, "Added item \"" + item.item_name + "\".")
        return redirect('add_item')

    return render(request, 'main/add_item.html')

