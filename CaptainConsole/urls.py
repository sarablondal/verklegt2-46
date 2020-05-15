"""CaptainConsole URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500

handler400 = 'errorhandling.views.view_400'
handler403 = 'errorhandling.views.view_403'
handler404 = 'errorhandling.views.view_404'
handler500 = 'errorhandling.views.view_500'
urlpatterns = [
    path('', include('frontpage.urls')), #til að fara beint á forsíðu
    path('admin/', admin.site.urls),
    path('consoles/', include('console.urls')),
    path('about_us/', include('about_us.urls')),
    path('cart/', include('cart.urls')),
    path('user/', include('user.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)