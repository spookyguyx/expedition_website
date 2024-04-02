from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
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
        context['photo'] = PhotoHome.objects.filter(photo_home_id__article_slug=slug)
        return context


@login_required(login_url='admin_login')
def upload_and_display_files(request, slug):
    files = PhotoHome.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                PhotoHome.objects.create(photo_home_id_id=Article.objects.get(article_slug=slug).id, photo_home=uploaded_file)
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
