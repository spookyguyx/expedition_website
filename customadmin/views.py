from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import *
from main.models import *


def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('admin_main/')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, 'Аккаунт не существует')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('admin_main/')



            messages.info(request, 'Недействительный пароль')
            return redirect('/')

        return render(request, 'admin_entrance.html')

    except Exception as e:
        print(e)


@login_required(login_url='admin_login')
def admin_main(request):
    return render(request, 'admin_main.html')


@login_required(login_url='admin_login')
def admin_exp_main(request):
    if request.method == 'GET':
        context = {
            'articles': Article.objects.all()
        }
        return render(request, 'admin_exp_main.html', context)
    pass


@login_required(login_url='admin_login')
def add_exp(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_exp')

    form = ArticlesForm()

    data = {
        'form': form,
    }

    return render(request, 'add.html', data)



class ItemsExpeditions(LoginRequiredMixin, DetailView):
    login_url = 'admin_login'
    redirect_field_name = '/'
    template_name = "admin_exp_items.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'


# @login_required(login_url='admin_login')
# def admin_team(request, slug):
#     if request.method == 'GET':
#         context = {
#             'team': Team.objects.filter(team_id__article_slug=slug)
#         }
#         return render(request, 'admin_team.html', context)
#     pass


@login_required(login_url='admin_login')
def admin_add_team(request, slug):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_team', slug)

    form = TeamForm(initial={'team_id': Article.objects.get(article_slug=slug).id})
    url = reverse("admin_team", kwargs={"slug": slug})
    data = {
        'form': form,
        'url_data': url,
    }

    return render(request, 'admin_team_add.html', data)


class Admin_team(LoginRequiredMixin, DetailView):
    template_name = "admin_team.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['team'] = Team.objects.filter(team_id__article_slug=slug)
        return context


class Admin_photo(LoginRequiredMixin, DetailView):
    template_name = "admin_photoarchive.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['photo'] = ArticleImage.objects.filter(post__article_slug=slug)
        return context


@login_required(login_url='admin_login')
def upload_and_display_files(request, slug):
    files = ArticleImage.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                ArticleImage.objects.create(post_id=Article.objects.get(article_slug=slug).id, images=uploaded_file)
            return redirect('admin_archive', slug)
    form = UploadFileForm()
    url = reverse("admin_archive", kwargs={"slug": slug})

    return render(request, 'admin_add_photoarchive.html', {'form': form, 'files': files, 'url_data': url})


class Admin_partners(LoginRequiredMixin, DetailView):
    template_name = "admin_partners.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['partners'] = Partners.objects.filter(partners_id__article_slug=slug)
        return context


@login_required(login_url='admin_login')
def admin_add_partners(request, slug):
    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_partners', slug)

    form = PartnersForm(initial={'partners_id': Article.objects.get(article_slug=slug).id})
    url = reverse("admin_partners", kwargs={"slug": slug})
    data = {
        'form': form,
        'url_data': url,
    }

    return render(request, 'admin_partners_add.html', data)


class Admin_maps(LoginRequiredMixin, DetailView):
    template_name = "admin_map.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['map'] = Map.objects.filter(post__article_slug=slug)
        return context


@login_required(login_url='admin_login')
def admin_add_map(request, slug):
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_map', slug)

    form = MapForm(initial={'post': Article.objects.get(article_slug=slug).id})
    url = reverse("admin_map", kwargs={"slug": slug})
    data = {
        'form': form,
        'url_data': url,
    }

    return render(request, 'add_map.html', data)


class Admin_events(LoginRequiredMixin, DetailView):
    template_name = "admin_events.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['event'] = Events.objects.filter(event_id__article_slug=slug)
        return context


@login_required(login_url='admin_login')
def admin_add_event(request, slug):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_events', slug)

    form = EventForm(initial={'event_id': Article.objects.get(article_slug=slug).id})
    url = reverse("admin_events", kwargs={"slug": slug})
    data = {
        'form': form,
        'url_data': url,
    }

    return render(request, 'admin_events_add.html', data)


class Admin_photo_home(LoginRequiredMixin, DetailView):
    template_name = "admin_photo.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['photo'] = PhotoHome.objects.filter(photo_home_id__article_slug=slug)
        return context


@login_required(login_url='admin_login')
def upload_photo(request, slug):
    files = PhotoHome.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                PhotoHome.objects.create(photo_home_id_id=Article.objects.get(article_slug=slug).id, photo_home=uploaded_file)
            return redirect('admin_photo', slug)
    form = UploadFileForm()
    url = reverse("admin_photo", kwargs={"slug": slug})

    return render(request, 'admin_add_photo.html', {'form': form, 'files': files, 'url_data': url})


class ArticleUpdateView(UpdateView, LoginRequiredMixin):
    model = Article
    template_name = 'add.html'
    form_class = ArticlesForm
    slug_field = 'article_slug'
    context_object_name = 'el'


class ArticleDeliteView(DeleteView, LoginRequiredMixin):
    model = Article
    template_name = 'delete.html'
    success_url = '/admin/admin_exp/'
    slug_field = 'article_slug'
    context_object_name = 'el'


@login_required(login_url='admin_login')
def admin_news(request):
    if request.method == 'GET':
        context = {
            'news': News.objects.all()
        }
        return render(request, 'admin_news.html', context)
    pass


@login_required(login_url='admin_login')
def admin_add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_news')

    form = NewsForm()
    data = {
        'form': form,
    }

    return render(request, 'admin_news_add.html', data)


class NewsUpdateView(UpdateView, LoginRequiredMixin):
    model = News
    template_name = 'admin_news_add.html'
    form_class = NewsForm


class Admin_result(LoginRequiredMixin, DetailView):
    template_name = "admin_result.html"
    model = Article
    slug_field = 'article_slug'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['result'] = ResultsExpedition.objects.filter(result__article_slug=slug)
        return context


@login_required(login_url='admin_login')
def admin_add_result(request, slug):
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_result', slug)

    form = ResultForm(initial={'result': Article.objects.get(article_slug=slug).id})
    url = reverse("admin_result", kwargs={"slug": slug})
    data = {
        'form': form,
        'url_data': url,
    }

    return render(request, 'admin_result_add.html', data)