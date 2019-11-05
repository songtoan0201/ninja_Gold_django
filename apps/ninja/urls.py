from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.calculate_gold),
    url(r'^destroy_session$', views.reset),
    url(r'^show$', views.show),
]
