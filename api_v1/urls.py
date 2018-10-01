from django.conf.urls import url

from api_v1 import views

urlpatterns = [
    url(r'^customers$', views.CreateCustomerAPIView.as_view(), name='create_customer')
]
