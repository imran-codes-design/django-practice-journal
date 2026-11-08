from django.shortcuts import render
from .forms import StudentForm


def home(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            student = {
                'name': form.cleaned_data['student_name'],
                'email': form.cleaned_data['email'],
                'age': form.cleaned_data['age'],
                'department': form.cleaned_data['department']
            }

            return render(
                request,
                'students/success.html',
                {'student': student}
            )

    else:
        form = StudentForm()

    return render(
        request,
        'students/register.html',
        {'form': form}
    )