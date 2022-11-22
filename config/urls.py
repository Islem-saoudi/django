
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('', include('backend.urls')),   
    path('', include('blog.urls')),
    path('', include('projects.urls')),
    path('', include('clients.urls')),
    path('', include('page.urls')),


    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'api.views.page_not_found_view'
handler500 = 'api.views.error_view'
handler403 = 'api.views.permission_denied_view'
handler400 = 'api.views.bad_request_view'
