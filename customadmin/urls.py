from django.urls import path
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
    path('admin_exp/<slug:slug>/archive/add_photo/', upload_and_display_files, name='add_photo'),
    path('admin_exp/<slug:slug>/partners/', Admin_partners.as_view(), name='admin_partners'),
    path('admin_exp/<slug:slug>/partners/add_partners', admin_add_partners, name='add_partners'),
    path('admin_exp/<slug:slug>/map/', Admin_maps.as_view(), name='admin_map'),
    path('admin_exp/<slug:slug>/map/add_map/', admin_add_map, name='add_map'),
    path('admin_exp/<slug:slug>/events/', Admin_events.as_view(), name='admin_events'),
    path('admin_exp/<slug:slug>/events/add_event/', admin_add_event, name='add_event'),
    path('admin_exp/<slug:slug>/photo/', Admin_photo_home.as_view(), name='admin_photo'),
    path('admin_exp/<slug:slug>/photo/add_image/', upload_photo, name='add_image'),
    path('admin_exp/<slug:slug>/update/', ArticleUpdateView.as_view(), name='admin_update'),
    path('admin_exp/<slug:slug>/delete/', ArticleDeliteView.as_view(), name='admin_delete'),
    path('admin_news/', admin_news, name='admin_news'),
    path('admin_news/add_news/', admin_add_news, name='admin_add_news'),
    path('admin_news/update/', NewsUpdateView.as_view(), name='update_news'),
    path('admin_exp/<slug:slug>/result/', Admin_result.as_view(), name='admin_result'),
    path('admin_exp/<slug:slug>/result/add_result', admin_add_result, name='add_result'),
]
