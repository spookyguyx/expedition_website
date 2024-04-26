from main.models import *
from django import forms


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name',
                  'name_long',
                  'text',
                  'current_expedition',
                  'photo_main_page',
                  'map',
                  'video',
                  'article_slug'
                  ]
        widgets = {'article_slug': forms.HiddenInput}


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_id',
                  'members_name',
                  'role_member',
                  'photo_members'
                  ]
        widgets = {'team_id': forms.HiddenInput}


class PartnersForm(forms.ModelForm):
    partners_id = forms.ModelMultipleChoiceField(
        queryset=Article.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Partners
        fields = [
                  'partners',
                  'photo_partners',
                  'partners_id',
                  ]


class NewsForm(forms.ModelForm):
    articles = forms.ModelMultipleChoiceField(
        queryset=Article.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = News
        fields = ['name',
                  'text',
                  'photo',
                  'video',
                  'news_slug',
                  'active_news',
                  'articles'
                  ]


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['photo']


class PhotoArchiveForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ['comment']


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_id',
                  'title_event',
                  'date_event',
                  'photo_events',
                  'description_event',
                  'slug',
                  ]


class ResultForm(forms.ModelForm):
    class Meta:
        model = ResultsExpedition
        fields = ['result',
                  'text_result',
                  'image'
                  ]
        widgets = {'result': forms.HiddenInput}


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class UploadFileForm(forms.Form):
    files = MultipleFileField()
    post = forms.HiddenInput()
