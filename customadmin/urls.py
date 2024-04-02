from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('admin_main/', admin_main, name='admin_main'),
    path('admin_exp/', admin_exp_main, name='admin_exp'),
    path('add_exp/', add_exp, name='add_exp'),
    path('admin_exp/<slug:slug>/', ItemsExpeditions.as_view(), name='add_exp_items'),
    path('admin_exp/<slug:slug>/team/', Admin_team.as_view(), name='admin_team'),
    path('admin_exp/<slug:slug>/team/add_exp_team/', admin_add_team, name='add_exp_team'),
    path('admin_exp/<slug:slug>/archive/', Admin_photo.as_view(), name='admin_archive'),
    path('admin_exp/<slug:slug>/archive/add_photo', upload_and_display_files, name='add_photo'),
    path('admin_exp/<slug:slug>/partners/', Admin_partners.as_view(), name='admin_partners'),
    path('admin_exp/<slug:slug>/partners/add_partners', admin_add_partners, name='add_partners')
]
