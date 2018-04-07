from django import forms


class ArticleEditForm(forms.Form):
    new_markup = forms.CharField(widget=forms.Textarea)
    pseudonym = forms.CharField(label='A name to remember you by', max_length=30)


class ArticleSearchForm(forms.Form):
    search_title = forms.CharField(label='', max_length=185)