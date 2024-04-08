from main.models import *
from django import forms


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name',
                  'name_long',
                  'text',
                  'current_expedition',
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
    class Meta:
        model = Partners
        fields = ['partners_id',
                  'partners',
                  'photo_partners',
                  ]
        widgets = {'partners_id': forms.HiddenInput}


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['post',
                  'maps',
                  ]
        widgets = {'post': forms.HiddenInput}


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name',
                  'text',
                  'photo',
                  'video',
                  'news_slug'

                  ]


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_id',
                  'title_event',
                  'date_event',
                  'photo_events',
                  'description_event',
                  'slug'
                  ]
        widgets = {'event_id': forms.HiddenInput}


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
