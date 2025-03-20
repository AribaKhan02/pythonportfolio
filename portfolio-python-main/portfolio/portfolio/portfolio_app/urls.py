from django.urls import path
from .  import views
urlpatterns = [
    path('', views.index,name='index'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('certificate/', views.Certificate_view, name='certificate'),
    path('certificates/<str:title>/', views.certificate_detail_view, name='certificate_detail'),
]
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

