from django.shortcuts import render
from .models import Person
from .forms import PersonForm

# Create your views here.
def app_home(request):
    

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    people = Person.objects.all()
    form = PersonForm()
    context={
        'people' : people,
         'form': form
        }

    return render(request,'webhome.html',context)