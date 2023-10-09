from django.urls import path
from .import views
from members import views as user_view

urlpatterns = [
    path('members/',views.members, name='members'),
    path('members/abcd/',views.abcd, name='abcd'),
    path('members/cake/',views.cake, name='cake'),
    path('members/contact/',views.contact, name='contact'),
    path('members/register/',views.register, name='register'),
    path('members/register/insertrecord/',views.insertrecord, name='insertrecord'),
    path('members/login/login_user',views.login_user, name='login_user '),
    path('members/login/register',views.register, name='register '),
    path('members/login/', user_view.login, name ='login'),
    path('members/login/insertrecord/', views.insertrecord, name ='insertrecord'),
    path('members/login/members', views.members, name ='members'),
    path('admin_data/', views.admin_data, name='admin_data'),
    path('admin_data/admin_form/', views.admin_form, name='admin_form'),
    path('admin_data/admin_login/', views.login, name='admin_login'),
    path('admin_data/admin_form/add_data/', views.add_data, name='add_data'),
    path('admin_data/admin_login/admin_checkdata/', views.admin_checkdata, name='admin_checkdata'),
    path('admin_data/admin_tables/delete/<int:id>', views.delete, name='delete'),
    path('admin_data/admin_tables/', views.admin_tables, name='admin_tables'),
    path('admin_data/admin_tables/update/<int:id>', views.update, name='update'),
    path('admin_data/admin_tables/update/updaterecord/<int:id>',views.updaterecord,name="updaterecord"),
    path('admin_data/user_data', views.user_data, name='user_data'),

    
]
