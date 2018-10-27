from django import forms
from . import models

class NewProblem(forms.ModelForm):
    class Meta():
        model = models.Problem
        fields = ["title", "statement", "source"]

class NewSolution(forms.ModelForm):
    class Meta():
        model = models.Solution
        fields = ["title", "language", "algorythm", "code"]
        widgets = {"algorythm": forms.Textarea(attrs={"cols": 100}), "code": forms.Textarea(attrs={"rows": 50, "cols": 105})}

