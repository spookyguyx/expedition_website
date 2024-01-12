from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('events/', EventsPage.as_view(), name='events'),
    path('publication/', PublicationPage.as_view(), name='publication'),
    path('separate_news/', Separate_newsPage.as_view(), name='separate_news'),
    path('photo/', PhotoPage.as_view(), name='photo'),
]