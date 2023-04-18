from django.conf.urls import url
from suchana import views
from django.urls import path

app_name = 'suchana'

urlpatterns=[
path('<int:id>',views.detailnews,name="detailnews"),
path('automobile/',views.getautomobile,name='automobile'),
path('techsiksha/',views.gettechsiksha,name='techsiksha'),
path('techdeals/',views.gettechdeals,name='techdeals'),
path('internet/',views.getinternet,name='internet'),
path('technews/',views.gettechnews,name='technews'),
path('techjobs/',views.gettechjobs,name='techjobs'),
path('gadgets/',views.getgadgets,name='gadgets'),
path('search/',views.search,name='search'),
]
