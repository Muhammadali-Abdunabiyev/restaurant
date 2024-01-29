from django.shortcuts import render, redirect
from foods.models import FoodsModel, EatModel
from pages.models import EventModel, CustomerModel, BookTableModels
from staff.models import ChefModel
from pages.forms import EmailModel, EmailForm, BookTableForms


def home_pages_views(request):
    special_food = FoodsModel.objects.filter(is_special=True).first()
    popular_foods = FoodsModel.objects.all()
    events = EventModel.objects.all()[:2]
    eats = EatModel.objects.all()
    customers = CustomerModel.objects.all()
    members = ChefModel.objects.all()
    context = {
        'abs': popular_foods,
        'special_food': special_food,
        'events': events,
        'eat': eats,
        'customers': customers,
        'members': members
    }
    return render(request, 'index.html', context=context)



def create_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_model = EmailModel.objects.filter(email=email).first()
            if not email_model:
                form.save()
                return redirect('/')
            else:
                return redirect(request, 'email-exists.html')
        else:
            return redirect(request, '/')
    else:
        return redirect(request,'/')



def create_booktable_view(request):
    if request.method == 'POST':
        form = BookTableForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_model = BookTableModels.objects.filter(email=email).first()
            if not email_model:
                form.save()
                return redirect('/')
            else:
                return redirect(request, 'email-exists.html')
        else:
            return redirect(request, '/')
    else:
        return redirect(request,'/')























