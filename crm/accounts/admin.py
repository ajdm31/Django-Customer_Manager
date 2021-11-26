from django.contrib import admin

# Register your models here.

#import from all the classes in the models.py file
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

