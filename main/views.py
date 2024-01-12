from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'main/main.html'
class EventsPage(TemplateView):
    template_name = 'main/events.html'
class PublicationPage(TemplateView):
    template_name = 'main/publication.html'
class Separate_newsPage(TemplateView):
    template_name = 'main/separate_news.html'
class PhotoPage(TemplateView):
    template_name = 'main/photo.html'

class ExpeditionPage(TemplateView):
    template_name = 'main/expedition.html'
class NewsPage(TemplateView):
    template_name = 'main/news.html'
class TeamPage(TemplateView):
    template_name = 'main/team.html'