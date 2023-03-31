# Import the `render` and `get_object_or_404` functions from the `django.shortcuts` module.
# Also import the `Item` model from the current directory (`.`).
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item

def items(request):
    items =Item.objects.filter(is_sold=False)
    
    return render(request, 'item/items.html', {'items': items})

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
    

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    
    return render(request, 'item/form.html', {'form': form, 'title': 'New item'})

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/form.html', {'form': form, 'title': 'Edit item'})

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')