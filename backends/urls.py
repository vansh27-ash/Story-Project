from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='Home'),
    path('create_story/',views.create_story,name='CreateStory'),
    path('about_us/',views.about_us,name='AboutUs'),
    path('my_story/',views.show_my_story,name='ShowMyStory'),
	
	path('example_1/',views.example_1,name='Exp1'),
    path('example_2/',views.example_2,name='Exp2'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)