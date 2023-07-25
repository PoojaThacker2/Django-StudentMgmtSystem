from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("school.urls")),
]
# urlpatterns = urlpatterns + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
# )