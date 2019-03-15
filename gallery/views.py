from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    

def gallery_of_day(request):
    date = dt.date.today()
    # gallery = Image.todays_gallery()
    return render(request, 'all-gallery/today-gallery.html', {"date": date})


def past_days_gallery(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_of_day)
        # gallery = Image.days_gallery(date)
    return render(request, 'all-gallery/past-gallery.html', {"date": date})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})