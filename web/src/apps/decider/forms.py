from django import forms
from .models import Site


class SiteForm(forms.Form):
    class Meta(UserCreationForm.Meta):
        model = Stie
        fields = ["url"]

