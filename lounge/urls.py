from django.contrib import admin
from django.urls import path
from django import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', LoungeListView.as_view(), name="lounge-ul-home"),

    path('create/', LoungeCreateView.as_view(), name='lounge-ul-create'),
    path('<int:pk>/', LoungeDetailView.as_view(), name='lounge-ul-detail'),
    path('<int:pk>/update/', LoungeUpdateView.as_view(), name='lounge-ul-update'),
    path('<int:pk>/delete/', LoungeDeleteView.as_view(), name='lounge-ul-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)