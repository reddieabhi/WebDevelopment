"""
URL configuration for WebDevelopment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from home.views import *
from veges.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('',djhtml),
    path('receipes',receipes),
    path('delete_reciepe/<id>/',delete_reciepe,name='delete_reciepe'),
    path('update_receipe/<id>/',update_receipe,name='update_receipe'),
    path('exist',exist),
    path('login_page',login_page,name='login_page'),
    path('logout_page',logout_page,name='logout_page'),
    path('register',register,name='register'),
    path('',abhi),
    path('abc',abc),
    path('new',new),
    path('contact',contact),
    path('about',about),
    path("admin", admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
