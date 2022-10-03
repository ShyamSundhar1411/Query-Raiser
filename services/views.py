from .models import Query
from django.shortcuts import render

# Create your views here.
def home(request):
    queries = Query.objects.filter(user = request.user)
    return render(request,"services/home.html",{"Queries":queries})