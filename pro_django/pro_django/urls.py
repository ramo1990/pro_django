from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, about_view, contact_view, product_detail_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cours/', include('cours.urls')),
]
