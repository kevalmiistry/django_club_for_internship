from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import homeview, logout, prodelete, productview, signupview, loginview, searchview, vendorinventoryview, vendorloginview, vendorlogout

urlpatterns = [

    path('signupview/', signupview, name='signupview'),
    path('loginview/', loginview, name='loginview'),
    path('homeview/', homeview, name='homeview'),
    path('productview/<int:abc>/', productview, name='productview'),
    path('prodel/<int:abc>/', prodelete, name='prodel'),
    path('searchview/', searchview, name='searchview'),
    path('logout/', logout, name='logout'),
    path('vendorlogout/', vendorlogout, name='vendorlogout'),
    path('vendorloginview/', vendorloginview, name='vendorloginview'),
    path('vendorinventoryview/', vendorinventoryview, name='vendorinventoryview'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)