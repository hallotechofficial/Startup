from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

app_name='app1'
urlpatterns = [
    path("",views.home, name="h"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("services",views.service, name="service"),
    path("Project/",views.project, name="project"),
] 

# Add configurations for serving media and static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
