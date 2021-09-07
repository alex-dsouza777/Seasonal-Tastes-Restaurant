"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings

urlpatterns = [
 path('admin/', admin.site.urls),
 path('profile/',include('userprofile.urls',namespace='profile')),
 path('logout/',include('login.urls',namespace='logout')),
 path('changepass/',include('changepassword.urls',namespace='changepass')),
 path('signup/',include('signup.urls',namespace='signup')),
 path('login/',include('login.urls',namespace='login')),
 path('meals/',include('meals.urls',namespace ='meals')),
 path('about-us/',include('aboutus.urls',namespace ='aboutus')),
 path('contact/',include('contact.urls',namespace ='contact')),
 path('blog/',include('blog.urls',namespace ='blog')),
 path('',include('home.urls',namespace ='home')),
 path('reserve_table/',include('reservation.urls',namespace ='reservation')),
 path('summernote/',include('django_summernote.urls')),
 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Resturant Admin Pannel"
