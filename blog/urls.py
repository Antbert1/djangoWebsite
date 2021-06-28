from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("about/", views.about, name="about"),
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),    
    path("test/", views.test, name="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
