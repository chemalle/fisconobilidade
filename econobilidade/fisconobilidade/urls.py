from django.conf.urls import url
from fisconobilidade import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]
