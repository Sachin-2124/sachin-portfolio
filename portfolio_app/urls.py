from django.urls import path
from . import views

urlpatterns = [
    # Public views
    path('', views.index_view, name='index'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),

    # Live Interactive Project Demos
    path('demo/tour/', views.demo_tour, name='demo_tour'),
    path('demo/smartresume/', views.demo_smartresume, name='demo_smartresume'),
    path('demo/stadium/', views.demo_stadium, name='demo_stadium'),
    path('demo/pg/', views.demo_pg, name='demo_pg'),

    # Custom Admin Dashboard Authentication
    path('panel/login/', views.admin_login_view, name='admin_login'),
    path('panel/forgot-password/', views.admin_forgot_password_view, name='admin_forgot_password'),
    path('panel/logout/', views.admin_logout_view, name='admin_logout'),

    # Custom Admin Dashboard Views
    path('panel/', views.admin_dashboard, name='admin_dashboard'),
    
    # Projects CRUD
    path('panel/projects/', views.admin_projects_list, name='admin_projects'),
    path('panel/projects/add/', views.admin_project_add, name='admin_project_add'),
    path('panel/projects/edit/<int:pk>/', views.admin_project_edit, name='admin_project_edit'),
    path('panel/projects/delete/<int:pk>/', views.admin_project_delete, name='admin_project_delete'),

    # Messages
    path('panel/messages/', views.admin_messages_list, name='admin_messages'),
    path('panel/messages/read/<int:pk>/', views.admin_message_toggle_read, name='admin_message_toggle_read'),
    path('panel/messages/delete/<int:pk>/', views.admin_message_delete, name='admin_message_delete'),

    # Profile & Info
    path('panel/profile/', views.admin_profile_edit, name='admin_profile'),

    # Education CRUD
    path('panel/education/', views.admin_education_list, name='admin_education'),
    path('panel/education/add/', views.admin_education_add, name='admin_education_add'),
    path('panel/education/edit/<int:pk>/', views.admin_education_edit, name='admin_education_edit'),
    path('panel/education/delete/<int:pk>/', views.admin_education_delete, name='admin_education_delete'),

    # Skills
    path('panel/skills/', views.admin_skills_list, name='admin_skills'),
    path('panel/skills/delete/<int:pk>/', views.admin_skill_delete, name='admin_skill_delete'),
]
