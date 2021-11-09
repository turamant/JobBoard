
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views
from apps.core.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('apps.userprofile.urls')),
    path('notifications/', include('apps.notification.urls')),
    path('jobs/', include('apps.job.urls')),
]
