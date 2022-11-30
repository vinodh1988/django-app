from django.shortcuts import render
from .models import Person
from .forms import PersonForm

# Create your views here.
def app_home(request):
    people = Person.objects.all()

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    form = PersonForm()
    context={
        'people' : people,
         'form': form
        }

    return render(request,'webhome.html',context)