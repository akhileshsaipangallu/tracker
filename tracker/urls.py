# Django
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

# local Django
from tracker import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view()),
    path('', include('project.urls')),
    path('task/', include('task.urls'))
]
