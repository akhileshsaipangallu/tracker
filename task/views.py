# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# local Django
from task.models import Task


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class TaskDetails(View):

    @staticmethod
    def get(request, task_id):
        """
        Task details handler
        :param request: Request object
        :param task_id: task id
        :return: Render object with task details
        """

        task_obj = get_object_or_404(Task, pk=task_id)

        # Request user and task-project creator check
        if request.user.pk != task_obj.project.created_by_id:
            if not request.user.groups.filter(name__iexact='user').exists():
                raise PermissionDenied

        user_auto_fill = User.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        ).values('id', 'full_name')

        return render(
            request,
            'task/task_details.html',
            {
                'task': task_obj,
                'user_auto_fill': user_auto_fill,
            }
        )

    @staticmethod
    def post(request, task_id):
        """
        Task edit handler
        :param request: Request object
        :param task_id: task
        :return: Render object with edited task details
        """

        task_obj = get_object_or_404(Task, pk=task_id)

        # Request user and task-project creator check
        if request.user.pk != task_obj.project.created_by_id:
            if not request.user.groups.filter(name__iexact='user').exists():
                raise PermissionDenied

        task_obj.assignee = get_object_or_404(
            User, pk=request.POST.get('assignee')
        )
        task_obj.save()

        user_auto_fill = User.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        ).values('id', 'full_name')

        return render(
            request,
            'task/task_details.html',
            {
                'task': task_obj,
                'user_auto_fill': user_auto_fill,
            }
        )
