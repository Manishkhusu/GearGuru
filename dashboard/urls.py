from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('', user_login, name='login'),
    path ('signup/', user_signup , name = 'signup'),
    path ('home/logout/' , logout_view , name = 'logout'),
    path('home/product/', product_page, name='product'),
    path('product/details/<int:product_id>/', detail_views, name='details')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
