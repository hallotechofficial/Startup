from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

app_name='app1'
urlpatterns = [
    path("",views.home, name="h"),
    path("about",views.about, name="about"),
    # path("/blog",views.blog, name="blog"),
    path("contact",views.contact, name="contact"),
    # path("/feature",views.feature, name="feature"),
    # path("/web_price",views.web_price, name="web"),
    # path("/hardware",views.hardware_price, name="hardware"),
    # path("/IOT",views.iot_price, name="iot"),
    # path("/AIML",views.ai_price, name="ai"),
    # path("/Media",views.media_price, name="media"),
    # path("/quote",views.quote, name="quote"),
    path("services",views.service, name="service"),
    # path("/team",views.team, name="team"),
    # path("/testimonial",views.testimonial, name="testimonial"),
    # path("/detail",views.detail, name="detail"),
    path("Project/",views.project, name="project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)