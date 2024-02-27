from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, show_product

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('show_product/<int:pk>/', show_product, name='show_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
