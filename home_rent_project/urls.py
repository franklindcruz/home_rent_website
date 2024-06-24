
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('adminuser/', include('admin_app.urls')),
    path('user/', include('user_app.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)