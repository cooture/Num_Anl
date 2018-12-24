from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [


    path('', views.upload),
    # path('show/', views.show),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)