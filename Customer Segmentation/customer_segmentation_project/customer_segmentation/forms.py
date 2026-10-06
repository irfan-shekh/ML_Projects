from django import forms
from .models import CustomerSegmentation

class CustomerSegmentationForm(forms.ModelForm):
    """Form for customer segmentation input"""
    
    class Meta:
        model = CustomerSegmentation
        fields = [
            'gender', 'ever_married', 'age', 'graduated', 'profession',
            'work_experience', 'spending_score', 'family_size', 'var_1'
        ]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'ever_married': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 18, 'max': 100}),
            'graduated': forms.Select(attrs={'class': 'form-select'}),
            'profession': forms.Select(attrs={'class': 'form-select'}),
            'work_experience': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 50, 'step': 0.1}),
            'spending_score': forms.Select(attrs={'class': 'form-select'}),
            'family_size': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20, 'step': 0.1}),
            'var_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Cat_4'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['work_experience'].required = False
        self.fields['family_size'].required = False
        self.fields['var_1'].required = False
        
        # Add help text
        self.fields['work_experience'].help_text = "Years of work experience (optional)"
        self.fields['family_size'].help_text = "Number of family members (optional)"
        self.fields['var_1'].help_text = "Category code (optional)"
        
        # Add placeholders
        self.fields['age'].widget.attrs['placeholder'] = "Enter age (18-100)"
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 100:
            raise forms.ValidationError("Age must be between 18 and 100")
        return age
    
    def clean_work_experience(self):
        work_experience = self.cleaned_data.get('work_experience')
        if work_experience is not None and (work_experience < 0 or work_experience > 50):
            raise forms.ValidationError("Work experience must be between 0 and 50 years")
        return work_experience
    
    def clean_family_size(self):
        family_size = self.cleaned_data.get('family_size')
        if family_size is not None and (family_size < 1 or family_size > 20):
            raise forms.ValidationError("Family size must be between 1 and 20")
        return family_size
