from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
]

# MEDIA_URL로 시작되는 요청이 오면 MEDIA_ROOT에서 파일을 찾아 serving 한다. static()리스트 반환
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path(r"^__debug__/", include(debug_toolbar.urls)),
    ]
