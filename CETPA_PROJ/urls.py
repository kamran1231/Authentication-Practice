
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('edit_profile/', views.edit_profile,name='edit_profile'),
    path('change_password/', views.change_password,name='change_password'),
]
