from django.conf.urls import url
from . import views
app_name = 'dimension'
urlpatterns=[
    url(r'^$',views.dim,name='dimension'),
]