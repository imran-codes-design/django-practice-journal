
from django import forms
class AdmissionForm(forms.Form):

    # Personal Information
    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@gmail.com',
            'class': 'form-control'
        })
    )

    phone = forms.CharField(
        max_length=15,
        label="Phone Number"
    )

    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    # Academic Information
    previous_qualification = forms.ChoiceField(
        choices=[
            ('matric', 'Matric'),
            ('intermediate', 'Intermediate'),
            ('bachelor', 'Bachelor'),
            ('master', 'Master'),
        ],
        label="Previous Qualification"
    )

    marks_percentage = forms.DecimalField(
        min_value=0,
        max_value=100,
        max_digits=5,
        decimal_places=2,
        label="Marks Percentage"
    )

    interested_program = forms.ChoiceField(
        choices=[
            ('bs_cs', 'BS Computer Science'),
            ('bs_it', 'BS Information Technology'),
            ('bs_ai', 'BS Artificial Intelligence'),
            ('bs_ds', 'BS Data Science'),
            ('bs_se', 'BS Software Engineering'),
        ],
        label="Interested Program",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    # Additional Information
    gender = forms.ChoiceField(
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        widget=forms.RadioSelect,
        label="Gender"
    )

    address = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Enter your complete address'
        }),
        label="Address"
    )

    agree_terms = forms.BooleanField(
        required=True,
        label="I agree to the terms and conditions"
    )
