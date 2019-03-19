from django.shortcuts import render,redirect
from .models import Image,Category,Location
# Create your views here.
    

def gallery(request):
    all_pictures = Image.all_pictures()
    locations = Location.objects.all()
    print(all_pictures)
    return render(request, 'gallery.html',{"all_pictures":all_pictures, 'locations':locations})


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

def display_location(request,location_id):
    try:
        location = Location.objects.get(id = location_id)
        images = Image.objects.filter(location = location.id)
        locations = Location.objects.all()
    except:
        raise Http404()
    return render(request,'location.html',{'location':location,'images':images, 'locations':locations})
