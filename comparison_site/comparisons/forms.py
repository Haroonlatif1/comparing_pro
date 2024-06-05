from django import forms
from .models import ComparisonTable, Product

class ComparisonTableForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = ComparisonTable
        fields = ['title', 'products']
