
from django.urls import path
from . import views
from .views import (
    #PostListView, # original home.html view
    ToDoListView,
    ToDoDetailView,
	ToDoCreateView,
	ToDoUpdateView,
    ToDoDeleteView,
    )
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url



urlpatterns = [
	
	path('', ToDoListView.as_view(), name='todo-home'),
    path('create/', ToDoCreateView.as_view(), name='todo-new'),
    path('<int:pk>/', ToDoDetailView.as_view(), name='todo-detail'),
    path('<int:pk>/update/', ToDoUpdateView.as_view(), name='todo-update'),
    path('<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo-delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

