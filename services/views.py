
from .models import Query
from . forms import QueryCreateForm
from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    queries = Query.objects.filter(user = request.user)
    return render(request,"services/home.html",{"Queries":queries})

def create_query(request):
    if request.method == "POST":
        query_form = QueryCreateForm(request.POST)
        if query_form.is_valid():
            query = query_form.save(commit=False)
            query.user = request.user
            query.status = "Pending Approval"
            query.save()
            messages.success(request,"Successfully raised a query. You will be notified about the status soon")
            return redirect("home")
        else:
            return render(request,"services/create_query.html",{"form":query_form,"hostride_form_errors":query_form.errors})
    else:
        return render(request,"services/create_query.html",{"form":QueryCreateForm()})