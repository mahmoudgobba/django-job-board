from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .models import Profile

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),name='logout'),
    path('profile/<str:username>/',views.UserProfile.as_view(),name='profile'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
]
