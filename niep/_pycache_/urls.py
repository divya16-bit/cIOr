"""warden URL Configuration

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
from django.urls import path
from loginapp import views
from django.conf import settings
from django.conf.urls.static import static
from loginapp.views import CompletePasswordReset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start, name='start'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('generate', views.generate, name='generate'),
    path('login_warden', views.login_warden, name='login_warden'),
    path('register_warden', views.register_warden, name='register_warden'),
    path('index_warden', views.scan, name='index_warden'),
    path('display', views.display, name='display'),
    path('resetpage', views.resetpage, name="resetpage"),
    path('request-password', views.password_reset_request, name='request-password'),
    path('set-new-password/<uidb64>/<token>', CompletePasswordReset.as_view(), name='reset-user-password'),
    path('logout', views.logout, name='logout'),
    path('logout1', views.logout1, name='logout1'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
