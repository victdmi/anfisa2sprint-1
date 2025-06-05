from django.contrib import admin

# Register your models here.
from .models import Category, Wrapper, Topping, IceCream

admin.site.register(Category)
admin.site.register(Wrapper)
admin.site.register(Topping)
admin.site.register(IceCream)