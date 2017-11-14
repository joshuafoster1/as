from django.conf.urls import url
from System_Designer import views
urlpatterns=[
    url(r'^home/$', views.SDhome, name="SDhome"),

]
