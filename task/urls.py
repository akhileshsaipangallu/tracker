# Django
from django.conf.urls import url

# local Django
from task import views

urlpatterns = [
    url(
        r'^(?P<task_id>\w+)/$',
        views.TaskDetails.as_view(),
        name='task_details'
    ),
]