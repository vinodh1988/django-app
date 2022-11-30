from django.shortcuts import render
from .models import Person

# Create your views here.
def app_home(request):
    people = Person.objects.all()
    context={
        'people' : people
    }

    return render(request,'webhome.html',context)