from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from views import *

urlpatterns = [
    url(r'^process$', ProcessView.as_view(), name="process_list"),
    url(r'^process/(?P<pk>[0-9]+)$', ProcessDetailsView.as_view(), name="process_details"),
    url(r'^stat$', StatView.as_view(), name="stats_list")
]
urlpatterns = format_suffix_patterns(urlpatterns)
