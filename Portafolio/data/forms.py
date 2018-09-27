from django import forms

class ProjectForm(forms.Form):
    title = forms.CharField(label = 'title', required = True,
        widget=forms.TextInput(attrs={'class':'border-radius',
         'placeholder':'title of your project'}))
    description = forms.CharField(label = 'description', required = True,
        widget=forms.Textarea(attrs={'class':'border-radius',
         'placeholder':'description of your project', 'rows':3}),
            min_length=10, max_length=120)
    image = forms.ImageField(label = 'image', required = True)
    link = forms.URLField(label = 'link', required = True)