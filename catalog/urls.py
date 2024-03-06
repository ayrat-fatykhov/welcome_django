from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView, BlogListView, BlogCreateView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', ContactsTemplateView.as_view()),
    path('show_product/<int:pk>/', ProductDetailView.as_view(), name='show_product'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
