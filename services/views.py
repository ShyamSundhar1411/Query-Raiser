
from .models import Query
from . forms import QueryCreateForm
from django.shortcuts import render

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