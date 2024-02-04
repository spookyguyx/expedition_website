from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('publication/', PublicationPage.as_view(), name='publication'),
    path('news/', NewsPage.as_view(), name='news'),
    path('addexp/', Add_expPage.as_view(), name='addexp'),
    path('news/<slug:slug>/', Separate_newsPage.as_view(), name='separate_news'),
    path('<slug:slug>/', ExpeditionPage.as_view(), name='expedition'),
    path('<slug:slug>/photo/', photo_page_view, name='photo'),
    path('<slug:slug>/map/', map_page_view, name='map'),
    path('<slug:slug>/team/', team_page_view, name='team'),
    path('<slug:slug>/events/', events_page_view, name='events'),
    path('<slug:slug>/result/', result_page_view, name='result')
]
