# forms.py
from django import forms
from .models import Criminal, Memory

class CriminalForm(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = ['name', 'crime_type', 'sentence_type']

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['empathy_level', 'regret_level', 'memory_description']
