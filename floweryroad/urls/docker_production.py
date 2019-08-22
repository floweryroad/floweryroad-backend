from .base import urlpatterns
import floweryroad.settings.docker_production as settings
from django.conf.urls.static import static

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)