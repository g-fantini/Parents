from django.shortcuts import render
from .forms import InsertNewPersonForm, PersonsTable
from django.http import HttpResponseRedirect
from .models import Person
import django_tables2 as tables
from django.db.models import Q

def home(response):
    return render(response,"main/home.html")

def insertPerson(response):     
    if response.method == "POST":
        form = InsertNewPersonForm(response.POST)
    
        #if form is valid create the record
        if form.is_valid():
            name = form.cleaned_data["name"] 
            date_of_birth = form.cleaned_data["date_of_birth"] 
            email = form.cleaned_data["email"] 
            n_of_childs = form.cleaned_data["n_of_childs"] 
            person = Person(name=name, date_of_birth=date_of_birth, email=email, n_of_childs=n_of_childs)
            person.save()
            return HttpResponseRedirect("/personsList")      
    else:
        form = InsertNewPersonForm()
    return render(response, "main/insert_person.html", {"form":form})

class personsList(tables.SingleTableView):
        
    table_class = PersonsTable
    #Sort the person by the number of childs (ascending)
    queryset = Person.objects.order_by("n_of_childs")
    template_name = "main/persons_list.html"
    #paginate the data when there are more than 15 rows
    table_pagination = {
        "per_page": 15
    }
    
    def get_table_data(self):
        return self.object_list
    
    def get_queryset(self):
        #Apply filter in case a search parameter is passed
        if(self.request.method == 'GET' and 'search' in self.request.GET):
            return Person.objects.filter(Q(name__contains=self.request.GET['search']) | Q(email__contains=self.request.GET['search']) ).order_by("n_of_childs")
        
        return Person.objects.filter().order_by("n_of_childs")
    
