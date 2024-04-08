from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import *
from django.utils.translation import gettext as _


class HomePage(ListView):
    template_name = 'main/main.html'
    queryset = Article.objects.all()
    # context_object_name = 'booba'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Anons.objects.all()
        for el in self.queryset:
            el.home_img = PhotoHome.objects.get(photo_home_id__article_slug=el.article_slug).photo_home.url
        context['articles'] = self.queryset
        return context


class PublicationPage(TemplateView):
    template_name = 'main/publication.html'


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


def partners_page_view(request, slug):
    if request.method == 'GET':
        context = {
            'partners': Partners.objects.filter(event_id__article_slug=slug)
        }
        return render(request, 'main/expedition.html', context)
    pass


def result_page_view(request, slug):
    if request.method == 'GET':
        context = {
            'results': ResultsExpedition.objects.filter(result__article_slug=slug)
        }
        return render(request, 'main/result.html', context)
    pass



class SearchPage(TemplateView):
    template_name = 'main/search.html'


class EventDetail(DetailView):
    model = Article
    template_name = 'main/seperate_event.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get('slug', None)
        event_slug = self.kwargs.get('event_slug', None)
        try:
            obj = queryset.get(article_slug=slug, events__slug=event_slug)
        except queryset.model.DoesNotExist:
            raise Http404(_("No Town found matching the query"))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['event'] = Events.objects.filter(event_id__article_slug=slug)
        return context