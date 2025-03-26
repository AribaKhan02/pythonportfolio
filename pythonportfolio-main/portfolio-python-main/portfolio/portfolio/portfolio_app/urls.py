from django.urls import path
from .  import views
urlpatterns = [
    path('', views.index,name='index'),
    path('resume/', views.resume_view, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('certificate/', views.Certificate_view, name='certificate'),
    path('certificates/<str:title>/', views.certificate_detail_view, name='certificate_detail'),
    path('download_resume/', views.download_resume, name='download_resume'),  # New URL for downloading CV
    path('certificate/delete/<int:id>/', views.delete_certificate, name='delete_certificate'),
    path('certificate/upload/', views.upload_certificate, name='upload_certificate'),
    path('blog/<title>/',views.blog_detail,name='blog_detail'),
    path('blog/',views.blog,name='blog'),
]
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

