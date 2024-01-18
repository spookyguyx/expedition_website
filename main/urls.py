from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('publication/', PublicationPage.as_view(), name='publication'),
    path('separate_news/', Separate_newsPage.as_view(), name='separate_news'),
    path('news/', NewsPage.as_view(), name='news'),
    path('<slug:slug>/', ExpeditionPage.as_view(), name='expedition'),
    path('<slug:slug>/photo/', photo_page_view, name='photo'),
    path('<slug:slug>/map/', map_page_view, name='map'),
    path('<slug:slug>/team/', team_page_view, name='team'),
    path('<slug:slug>/events/', events_page_view, name='events'),
]
