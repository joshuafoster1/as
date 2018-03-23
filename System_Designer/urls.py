from django.conf.urls import url
from System_Designer import views
urlpatterns=[
    url(r'^home/$', views.SDhome, name="SD_home"),
    url(r'^load/$', views.SD_load, name="SD_load"),
    url(r'^preferences/$', views.SD_preferences, name="SD_preferences"),
    url(r'^install/$', views.SD_install, name="SD_install"),
    url(r'^summary/$', views.SD_summary, name="SD_summary"),
    url(r'^recommendation/$', views.SD_recomendation, name="SD_recommendation"),
    url(r'^locations/$', views.SD_locations, name="SD_locations"),
    url(r'^createDP/$', views.create_DP, name = 'create_DP'),
]
