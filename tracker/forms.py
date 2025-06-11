from django import forms
from .models import Branch, Repository

class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ['name', 'description']

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name']