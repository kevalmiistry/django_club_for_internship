from django.urls import path
from .views import home, records  

urlpatterns = [
    path('home/', home, name='bs_home'),
    path('records/', records, name='bs_records')
]