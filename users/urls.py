
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	# func-based view
    path('register/', views.register, name='register' ),
    path('<username>', views.profile, name='profile' ),
    path('<username>/edit/', views.profile_edit, name='profile-edit' ),

    #path('<username>/test/', views.profile_test, name='profile-test' ),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
