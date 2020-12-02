from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
# from .views import LandingPageListView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from blog.views import BlogIndexView

urlpatterns = [
	# func-based view
    path('', views.landing, name='landing' ),
    path('home/', views.home, name='home' ),
    path('blog/', include('blog.urls') ),

    # get this done with pinax.announcements & pinax.templates
    # class-based detail view needed? check blog templates
    path('announcements/<int:pk>/', views.announcement, name='announcement-detail'),

    # testing func-based views
    path('test/', views.testing, name='testing' ),

    # testing class-based views
    # path('asdf/', LandingPageListView.as_view(), name='landingpagelistview')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
