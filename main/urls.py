from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('publication/', PublicationPage.as_view(), name='publication'),
    path('news/', NewsPage.as_view(), name='news'),
    path('addexp/', Add_expPage.as_view(), name='addexp'),
    path('adminent/', Admin_entrancePage.as_view(), name='adminent'),
    path('adminmain/', Admin_mainPage.as_view(), name='adminmain'),
    path('adminexpmain/', Admin_exp_mainPage.as_view(), name='adminexpmain'),
    path('adminexpitems/', Admin_exp_itemsPage.as_view(), name='adminexpitems'),
    path('adminpartners/', Admin_partnersPage.as_view(), name='adminpartners'),
    path('adminpartnersadd/', Admin_partners_addPage.as_view(), name='adminpartnersadd'),
    path('adminteam/', Admin_teamPage.as_view(), name='adminteam'),
    path('adminteamadd/', Admin_team_addPage.as_view(), name='adminteamadd'),
    path('adminevents/', Admin_eventsPage.as_view(), name='adminevents'),
    path('admineventsadd/', Admin_events_addPage.as_view(), name='admineventsadd'),
    path('adminphotoarchive/', Admin_photoarchivePage.as_view(), name='adminphotoarchive'),
    path('adminphotoarchivecomm/', Admin_photoarchive_commPage.as_view(), name='adminphotoarchivecomm'),
    path('adminnews/', Admin_newsPage.as_view(), name='adminnews'),
    path('adminnewsadd/', Admin_news_addPage.as_view(), name='adminnewsadd'),
    path('adminpublications/', Admin_publicationsPage.as_view(), name='adminpublications'),
    path('adminpublicationsadd/', Admin_publications_addPage.as_view(), name='adminpublicationsadd'),
    path('search/', SearchPage.as_view(), name='search'),
    path('news/<slug:slug>/', Separate_newsPage.as_view(), name='separate_news'),
    path('<slug:slug>/', ExpeditionPage.as_view(), name='expedition'),
    path('<slug:slug>/photo/', photo_page_view, name='photo'),
    path('<slug:slug>/map/', map_page_view, name='map'),
    path('<slug:slug>/team/', team_page_view, name='team'),
    path('<slug:slug>/events/', events_page_view, name='events'),
    path('<slug:slug>/result/', result_page_view, name='result'),
]
