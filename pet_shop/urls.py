"""pet_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shops import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('pets/list/',views.pet_list ,name='pet-list'),
    path('pets/<int:pet_id>/detail/',views.pet_detail ,name='pet-detail'),

    path('pets/create/',views.pet_create ,name='pet-create'),
    path('pets/<int:pet_id>/update/',views.pet_update ,name='pet-update'),
    path('pets/<int:pet_id>/delete/',views.pet_delete ,name='pet-delete'),

    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
    path('no-access/',views.no_access ,name='no-access'),

]
if settings.DEBUG:
    '''Uncomment the next line to include your static files'''
    # urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

