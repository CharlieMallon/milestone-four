# pylint: disable=missing-module-docstring
from cgitb import handler
from django.contrib import admin
from django.urls import path, include
# import static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('gallery/', include('gallery.urls')),
    path('faqs/', include('faqs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #static files being imported

handler404 = "home.views.handle_not_found"
handler500 = "home.views.handle_server_error"
