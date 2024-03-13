from django.urls import path
from . import views

urlpatterns = [
    path('admin_login/',views.AdminLoginView.as_view(), name='admin_login'),
    path('user_login/',views.UserLoginView.as_view(), name='user_login'),
    path('admin/create_admin/',views.AdminCreateUserView, name='create_user'),
    path('admin/create_staff/',views.StaffCreateUserView, name='create_staff'),
]