from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm


# Create your views here.
def index(request):
    my_dict = {
        'insert_me': "Jai Meher Baba, Hello World"
    }
    return render(request, 'index.html', context=my_dict)


def help(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'help.html', context=context)


def form_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            print("Validation Success")
            print(f"First Name: {form.cleaned_data['first_name']}")
            print(f"Last Name: {form.cleaned_data['last_name']}")
            print(f"Email: {form.cleaned_data['email']}")
            form.save(commit=True)
        else:
            print("ERROR FORM INVALID")
            return index(request)

    return render(request, 'user.html', {'form': form})
