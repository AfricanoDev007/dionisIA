from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("chat/", include('poetic_assitant.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='chat/', permanent=True)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
