from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import ListView, ListDetailView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lists/$', ListView.as_view(), name="all_lists"),
    url(r'^detail/(?P<pk>\d+)', ListDetailView.as_view(), name="list_detail"),
    
    # url(r'^new/$', new_list, name="new_list"),
    # url(r'^(?P<list_id>\d+)/destroy/$', delete_list, name="delete_list"),
    # url(r'^(?P<list_id>\d+)/detail/$', detail_list, name="list_detail"),
    # url(r'^(?P<list_id>\d+)/update/$', edit_list, name="edit_list"),
    # url(r'^(?P<list_id>\d+)/new-item/$', new_item, name="new_item"),
    # url(r'^(?P<item_id>\d+)/delete-item/$', delete_item, name="delete_item"),

)
