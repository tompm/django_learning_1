from django.conf.urls import url
from Hello import views

urlpatterns = [
	url(r'^helloworld/$',views.Hello_list),
	url(r'^helloworld/?P<pk>[0-9]+/$', views.Hello_detail),
]
