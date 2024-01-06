"""
URL configuration for swapsaman project.

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
from django.urls import path
from myapp import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("login/", views.signin, name="signin"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("post-ad/", views.post_ad, name="post_ad"),
    path("my_ads/", views.my_ads, name="my_ads"),
    path("guide/", views.guide, name="guide"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("category/<int:category_id>/", views.category_page, name="category_page"),
    path("product/<slug>/", views.view_ad, name="view_ad"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
