
from .models import Query
from . forms import QueryCreateForm
from django.contrib import messages
from django.views import generic
from django.shortcuts import get_object_or_404, render,redirect
from django.http.response import Http404, HttpResponse

# Create your views here.
#Class Based Views
class QueryDetailView(generic.DetailView):
    model = Query
    template_name = "services/ViewQuery.html"
    fields = ['title','description','date_of_creation','user','type','department']
    def get_object(self):
        query = super(QueryDetailView,self).get_object()
        if  (query.user == self.request.user) or (self.request.user.profile.role == "Program Representative"):
            return query
        raise Http404
#Function Based Views
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

def approve_query(request,pk,slug):
    query = Query.objects.get(id = pk,slug = slug)
    if request.method == "POST" and request.user.profile.role == "Program Representative":
        query.status = "Approved"
        query.save()
        messages.success(request,"Approved Query successfully")
        return redirect("query_detail_view",pk = pk,slug = slug)
    else:
        messages.error(request,"Error Processing Request")
        return redirect("query_detail_view",pk = pk,slug = slug)
def reject_query(request,pk,slug):
    query = Query.objects.get(id = pk,slug = slug)
    if request.method == "POST" and request.user.profile.role == "Program Representative":
        query.status = "Rejected"
        query.save()
        messages.success(request,"Rejected Query successfully")
        return redirect("query_detail_view",pk = pk,slug = slug)
    else:
        messages.error(request,"Error Processing Request")
        return redirect("query_detail_view",pk = pk,slug = slug)