
from django.urls import path, include

# from django documentation -- check CoreyMS' tutorial Part 8 / 22:30
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    #PostListView, # original home.html view
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    BlogIndexView,

    )
#from django.views.generic import FormView # for pagedown
#from .forms import BlogPostForm


urlpatterns = [
    path('', BlogIndexView.as_view(), name="blog-home"),             # home for blog app
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/detail/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/detail/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # filters applied to posts
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

