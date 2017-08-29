from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.KoshIndex.as_view(), name='index'),
    url(r'^meaning/(?P<pslug>[^\x00-\x7F]*[/~]*[^\x00-\x7F]*)$', views.WordMeaning.as_view(), name='meaning'),
    #url(r'^download$',views.BlogDownload.as_view(), name="download"),
]

handler404 = 'nepali.views.handler404'
