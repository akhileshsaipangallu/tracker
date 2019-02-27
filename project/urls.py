# Django
from django.conf.urls import url

# local Django
from project import views

urlpatterns = [
    url('^$', views.ProjectListing.as_view(), name='project_listing'),
    url(
        r'^project/(?P<project_id>\w+)$',
        views.ProjectDetails.as_view(),
        name='project_details'
    ),
]