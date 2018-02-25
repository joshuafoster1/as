from django.conf.urls import url
from System_Designer import views
urlpatterns=[
    url(r'^home/$', views.SDhome, name="SDhome"),
    url(r'^load/$', views.SD_load, name="SD_load"),
    url(r'^preferences/$', views.SD_preferences, name="SD_prefernces"),
    url(r'^install/$', views.SD_install, name="SD_install"),
    url(r'^summary/$', views.SD_summary, name="SD_summary"),
    url(r'^reccommendation/$', views.SD_reccomendation, name="SD_reccommendation"),

]
