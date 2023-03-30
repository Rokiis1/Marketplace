# Import the `render` and `get_object_or_404` functions from the `django.shortcuts` module.
# Also import the `Item` model from the current directory (`.`).
from django.shortcuts import render, get_object_or_404

from .models import Item

# Define a view function that takes a `request` object and a `pk` parameter.
# This function retrieves an `Item` object with the given primary key (`pk`)
# from the database, or raises a 404 error if it doesn't exist.
# It also retrieves up to 3 other `Item` objects that have the same category
# as the original item and are not sold, to display as related items.
# Finally, it renders a template called `item/detail.html` and passes
# the `item` and `related_items` objects to the template.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detail.html', {'item': item, "related_items": related_items})
    
