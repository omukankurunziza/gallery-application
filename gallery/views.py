from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location
# Create your views here.
    

def gallery(request):
    all_pictures = Image.all_pictures()
    print(all_pictures)
    return render(request, 'gallery.html',{"all_pictures":all_pictures})


def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})

def display_images_categories(request):    
    pictures = Image.picture_categories()

    return render(request, 'category.html', {"pictures":pictures}) 

def display_images_locations(request):    
    pictures = Image.picture_locations()

    return render(request, 'location.html', {"pictures":pictures}) 

def single_picture(request):
    image = Image.get_picture(image_id)
    return render(request, 'single_picture.html', {"image":image})