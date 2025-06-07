"""Source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static

# Now, we need to set an url, for the endpoint For that we need to import router :
from rest_framework import routers


# Now, we need to import the ViewSet we set in Core.views:
import Core.views

from Core.Auth import viewSets
from Beats.views import BeatViewSet
from Source import settings
# Creating a Router for my endpoint :
router = routers.DefaultRouter()

# Adding the ViewSet to the Router and setting the url:
router.register(r"user", Core.views.UserViewSet, 'user')
router.register(r"auth/register", viewSets.RegisterViewSet, basename='auth-register')
router.register(r"auth/login", viewSets.LoginViewSet, basename='auth-login')
router.register(r"auth/refresh", viewSets.RefreshViewSet, basename='auth-refresh')
router.register(r"beats", BeatViewSet, basename='beats')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Important to add all the urls of our URL :

    path('api-auth/', include('rest_framework.urls')),    
    path('api/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)