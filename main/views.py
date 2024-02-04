from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class Add_expPage(TemplateView):
    template_name = 'main/add.html'

class HomePage(ListView):
    template_name = 'main/main.html'
    queryset = Article.objects.all()
    context_object_name = 'articles'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Anons.objects.all()
        return context


#class EventsPage(TemplateView):
#    template_name = 'main/events.html'


class PublicationPage(TemplateView):
    template_name = 'main/publication.html'


#class Separate_newsPage(TemplateView):
#    template_name = 'main/separate_news.html'


class ExpeditionPage(DetailView):
    template_name = "main/expedition.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['images'] = PhotoHome.objects.filter(photo_home_id__article_slug=slug)
        return context





# class PhotoPage(ListView):
#     template_name = 'main/photo.html'
#     queryset = Article.objects.all()
#     context_object_name = 'archive'


def photo_page_view(request, slug):
    if request.method == 'GET':
        context = {
            'archive': ArticleImage.objects.filter(post__article_slug=slug)
        }
        return render(request, 'main/photo.html', context)
    pass


class NewsPage(ListView):
    template_name = 'main/news.html'
    queryset = News.objects.all()
    context_object_name = 'news'


class Separate_newsPage(DetailView):
    template_name = "main/separate_news.html"
    model = News
    slug_field = 'news_slug'
    context_object_name = 'el'


#class TeamPage(TemplateView):
#    template_name = 'main/team.html'


#class MapPage(TemplateView):
#   template_name = 'main/map.html'


def map_page_view(request, slug):
    if request.method == 'GET':
        context = {
            'map': Map.objects.filter(post__article_slug=slug)
        }
        return render(request, 'main/map.html', context)
    pass


def team_page_view(request, slug):
    if request.method == 'GET':
        context = {
            'team': Team.objects.filter(team_id__article_slug=slug)
        }
        return render(request, 'main/team.html', context)
    pass


def events_page_view(request, slug):
    if request.method == 'GET':
        context = {
            'event': Events.objects.filter(event_id__article_slug=slug)
        }
        return render(request, 'main/events.html', context)
    pass


#def partners_page_view(request, slug):
 #   if request.method == 'GET':
 #       context = {
 #           'partners': Partners.objects.filter(event_id__article_slug=slug)
  #      }
#        return render(request, 'main/expedition.html', context)
 #   pass


def result_page_view(request, slug):
    if request.method == 'GET':
        context = {
            'results': ResultsExpedition.objects.filter(result__article_slug=slug)
        }
        return render(request, 'main/result.html', context)
    pass

class SearchPage(TemplateView):
    template_name = 'main/search.html'