from django.conf.urls import url

from api_v1 import views

urlpatterns = [
    url(r'^customers$', views.CustomerListCreateAPIView.as_view(), name='customer_create'),
]
