from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
    url('^$',views.gallery,name='gallery'),
    url(r'^categories/', views.display_images_categories, name = 'categories'),
    url(r'^location/(\d+)',views.display_location,name='displayLocation'),
    url(r'^search/', views.search_results, name = 'search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)