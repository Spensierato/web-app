from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('o_journal/', include('o_journal.urls')),
	path('grappelli/', include('grappelli.urls')),
	path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
