"""dj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django nclude, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dj1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
	path('admin/', admin.site.urls),
    path('turnos/',include('turnos.urls')),
]
=======
	#path('admin/', admin.views)
    path('home/', views.homeview),
    path('turnos/',include('turnos.urls')),
    path('templates/Layout.html', views.layoutview),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> front_dev
