from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from .forms import InsertForm
def not_found(request):
    return HttpResponseNotFound("STudent record not found")
def indexPage(request):
    return render(request, "core/index.html")
def insertForm(request):
    if request.method == "POST":
        form = InsertForm(request.POST)

        if form.is_valid():
            request.session["product"] = form.cleaned_data
            return redirect("displayProduct")
        else:
            print(form.errors)
    else:
        form = InsertForm()

    return render(request, "core/insertForm.html", {"form": form})


def displayProduct(request):
    product = request.session.get("product")

    if product is None:
        return redirect("insertForm")

    return render(request, "core/displayProduct.html", {"product": product})
