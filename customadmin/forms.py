from main.models import *
from django import forms


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name',
                  'name_long',
                  'text',
                  'photo_main_page',
                  'current_expedition',
                  'video',
                  'article_slug'
                  ]


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
    photo_home_id = forms.HiddenInput()



