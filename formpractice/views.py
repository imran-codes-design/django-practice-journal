
from django.shortcuts import render
from .forms import AdmissionForm


def admission_form(request):

    if request.method == 'POST':

        form = AdmissionForm(request.POST)

        if form.is_valid():

            admission_data = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'date_of_birth': form.cleaned_data['date_of_birth'],
                'qualification': form.cleaned_data['previous_qualification'],
                'marks': form.cleaned_data['marks_percentage'],
                'program': form.cleaned_data['interested_program'],
                'gender': form.cleaned_data['gender'],
                'address': form.cleaned_data['address'],
                'agree_terms': form.cleaned_data['agree_terms'],
            }

            return render(
                request,
                'formpractice/success.html',
                {'admission': admission_data}
            )

    else:
        form = AdmissionForm()

    return render(
        request,
        'formpractice/admission.html',
        {'form': form}
    )
