from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('drone.urls')),  # rent a drone process
    path('rented/', include('rented.urls')),  # rented drone process
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # login and register app
    path('__reload__/', include('django_browser_reload.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
