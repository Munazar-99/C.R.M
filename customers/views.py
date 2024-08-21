from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Customer
from .forms import CustomerForm


# Create your views here.
def index(request):
    return render(
        request, "customers/index.html", {"customers": Customer.objects.all()}
    )


def view_customer(request, id):
    customer = Customer.objects.get(customer_id=id)
    return HttpResponseRedirect(reverse("index"))


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer_id = form.cleaned_data["customer_id"]
            new_first_name = form.cleaned_data["first_name"]
            new_last_name = form.cleaned_data["last_name"]
            new_email = form.cleaned_data["email"]
            new_phone_number = form.cleaned_data["phone_number"]

        new_customer = Customer(
            customer_id=new_customer_id,
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,
            phone_number=new_phone_number,
        )
        new_customer.save()
        return render(
            request,
            "customers/add_customer.html",
            {
                "form": CustomerForm(),
                "success": True,
            },
        )
    else:
        form = CustomerForm()
        return render(
            request,
            "customers/add_customer.html",
            {
                "form": CustomerForm(),
            },
        )


def edit_customer(request, id):
    if request.method == "POST":
        customer = Customer.objects.get(customer_id=id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return render(
                request, "customers/edit_customer.html", {"form": form, "success": True}
            )
    else:
        customer = Customer.objects.get(customer_id=id)
        form = CustomerForm(instance=customer)
    return render(
        request,
        "customers/edit_customer.html",
        {
            "form": form,
        },
    )

def delete_customer(request, id):
    if request.method == "POST":
        customer = Customer.objects.get(customer_id=id)
        customer.delete()
        return HttpResponseRedirect(reverse('index'))
