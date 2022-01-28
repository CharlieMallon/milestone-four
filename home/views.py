from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to render the index page """
    
    return render(request, 'home/index.html')


def manage_shop(request):
    """ A view to render the shop manager """
    
    return render(request, 'home/manage.html')