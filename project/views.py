# Django
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Value
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils.decorators import method_decorator

# local Django
from project.models import Project


@method_decorator(login_required, name='dispatch')
class ProjectListing(View):

    @staticmethod
    def get(request):
        """
        Project listing handler
        :param request: Request object
        :return: Render object with projects
        """

        projects = Project.objects.annotate(
            task_count=Count('task')
        )

        return render(
            request, 'project/project_listing.html', {'projects': projects}
        )


@method_decorator(login_required, name='dispatch')
class ProjectDetails(View):

    @staticmethod
    def get(request, project_id):
        """
        Project details handler
        :param request: Request object
        :param project_id: project id
        :return: Render object with project tasks
        """

        project_obj = get_object_or_404(Project, pk=project_id)

        # Request user and project creator check
        if request.user.pk != project_obj.created_by_id:
            if not request.user.groups.filter(name__iexact='user').exists():
                raise PermissionDenied

        project_tasks = project_obj.task_set.all().annotate(
            assignee_name=Concat(
                'assignee__first_name', Value(' '), 'assignee__last_name'
            )
        )

        return render(
            request,
            'project/project_details.html',
            {
                'project_tasks': project_tasks,
                'project_name': project_obj.name
            }
        )
