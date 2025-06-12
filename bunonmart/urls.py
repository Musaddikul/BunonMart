from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts.views import RegisterView
from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path("register/", RegisterView.as_view(), name="register"),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('men/', views.men_page, name='men'),
    path('women/', views.women_page, name='women'),
    path('kids/', views.kids_page, name='kids'),
    path('eid/', views.eid_collection, name='eid'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
