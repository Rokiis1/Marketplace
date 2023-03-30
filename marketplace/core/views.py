# Import the SignUpForm model and the redirect function
from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignUpForm

# Define a view for the homepage
def index(request):
    # Get the first six unsold items
    items = Item.objects.filter(is_sold=False)[0:6]
    # Get all categories
    categories = Category.objects.all()
    # Render the homepage template with the items and categories
    return render(request, 'core/index.html', {'items': items, 'categories': categories})

# Define a view for the contact page
def contact(request):
    # Render the contact page template
    return render(request, 'core/contact.html')

# Define a view for the signup page
def signup(request):
    # If the form has been submitted
    if request.method == 'POST':
        # Create a new SignUpForm instance with the data from the request
        form = SignUpForm(request.POST)
        # If the form is valid
        if form.is_valid():
            # Save the form to the database
            form.save()
            # Redirect the user to the login page
            return redirect("/login/")
    # If the form has not been submitted
    else:
        # Create a new, empty SignUpForm instance
        form = SignUpForm()
        
    # Render the signup page template with the form as context
    return render(request, 'core/signup.html', {'form': form})
