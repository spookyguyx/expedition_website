from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'main/main.html'
class EventsPage(TemplateView):
    template_name = 'main/events.html'
class PublicationPage(TemplateView):
    template_name = 'main/publication.html'
class Separate_newsPage(TemplateView):
    template_name = 'main/Separate_news.html'