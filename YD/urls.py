from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/', include('account.urls')),
    # path('organization/', include('organization.urls')),
    path('master/', include('master.urls')),
    path('', include('search.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
