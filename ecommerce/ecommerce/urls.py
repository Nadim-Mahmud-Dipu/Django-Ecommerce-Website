from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from .views import *
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact/', contact_page, name="contact"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('products/', ProductListView.as_view()),
    path('products-fbv/', product_list_view),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products-fbv/<int:pk>', product_detail_view),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
