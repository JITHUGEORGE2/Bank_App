from django import forms
from .models import Branch, District, PersonalInformation

class YourForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['name', 'dob', 'age', 'gender', 'phone', 'email', 'address', 'district', 'branch', 'account_type', 'debit_card', 'credit_card', 'cheque_book']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(YourForm, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.all()
        self.fields['branch'].queryset = Branch.objects.all()

    
