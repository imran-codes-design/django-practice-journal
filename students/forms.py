from django import forms


class StudentForm(forms.Form):

    student_name = forms.CharField(
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    age = forms.IntegerField(
        min_value=16,
        max_value=60
    )

    department = forms.ChoiceField(
        choices=[
            ('computer science','Computer Science'),
            ('Software Engineering', 'Software Engineering'),
            ('IT', 'Information Technology'),
            ('Datascience','Datascince')
        ]
    )