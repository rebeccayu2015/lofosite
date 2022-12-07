from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    curr_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='curr')
    time_found = models.DateTimeField(auto_now_add=True)
    where_found = models.CharField(max_length=100)
    where_left = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='items/')
    claim_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claim', null=True, blank=True)
    time_claimed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)
