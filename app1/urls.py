from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app1'
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.service, name="service"),
    path("project/", views.project, name="project"),
]

# Serve media files only during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
