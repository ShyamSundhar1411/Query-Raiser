

from . models import *
from . forms import *
from . filters import *
from . tasks import *
from datetime import date
from django.db.models import Q
from django.contrib import messages
from django.views import generic
from django.http.response import Http404, HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import get_object_or_404, render,redirect
from . aiding_functions import admitted_year_finder, email_checker, email_parser, is_program_representative
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#Class Based Views
class QueryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Query
    template_name = "services/ViewQuery.html"
    fields = ['title','description','date_of_creation','user','type','department']
    def get_object(self):
        query = super(QueryDetailView,self).get_object()
        if  (query.user == self.request.user) or (is_program_representative(self.request.user)):
            return query
        raise Http404
    def get_context_data(self, **kwargs):
        context = super(QueryDetailView, self).get_context_data(**kwargs)
        context['program_representatives'] = Profile.objects.filter(role = "Program Representative",department = self.request.user.profile.department,admitted_year = self.request.user.profile.admitted_year)
        return context
#Function Based Views
def landing_page(request):
    if request.user.is_authenticated:
        return redirect("portal")
    return render(request,"services/landing_page.html")
def home(request):
    if request.user.profile.department == None or request.user.profile.contact == None:
        messages.info(request,"Verify your account by adding Contact Number before proceeding to the portal")
        return redirect("profile",slug = request.user.profile.slug)
    if request.user.profile.role == 'Unauthorized':
        messages.error(request,"Your account is not authorized by the system. Kindly contact the administrator")
        return redirect("profile",slug = request.user.profile.slug)
    else:
        if is_program_representative(request.user):
            queries =  BiasedQueryFilter(request.GET,queryset = Query.objects.filter(department = request.user.profile.department,admitted_year = request.user.profile.admitted_year,).order_by('-date_of_creation'))
        else:
            queries = BiasedQueryFilter(request.GET,Query.objects.filter(user = request.user).order_by('-date_of_creation'))
        return render(request,"services/home.html",{"Queries":queries})
def handler_not_found(request,exception):
    return render(request,'services/404.html')
@login_required
@user_passes_test(lambda user:user.profile.department != 'Unauthorized' or user.profile.department != 'Unauthorized')
def create_query(request):
    if request.user.profile.contact == None or request.user.profile.department == None:
        messages.info(request,"Verify your profile by adding your contact before posting the query")
        return redirect("profile",slug=request.user.profile.slug)
    query_count = Query.objects.filter(user = request.user,status = "Pending Approval",date_of_creation__date =  date.today()).count()
    if query_count >=3:
        messages.info(request,"You are given a one-day query cooldown due to stacked up pending queries. Your query's timer will be reset. tommorrow")
        return redirect("home")
    if request.method == "POST":
        query_form = QueryCreateForm(request.POST)
        if query_form.is_valid():
            query = query_form.save(commit=False)
            query.user = request.user
            query.status = "Pending Approval"
            query.department = request.user.profile.department
            query.admitted_year = request.user.profile.admitted_year
            query.save()
            messages.success(request,"Successfully raised a query. You will be notified about the status soon")
            return redirect("portal")
        else:
            return render(request,"services/create_query.html",{"form":query_form,"hostride_form_errors":query_form.errors})
    else:
        return render(request,"services/create_query.html",{"form":QueryCreateForm()})
@login_required
@user_passes_test(lambda user:user.profile.department != 'Unauthorized' or user.profile.department != 'Unauthorized')
def approve_query(request,pk,slug):
    query = Query.objects.get(id = pk,slug = slug)
    if request.method == "POST" and is_program_representative(request.user):
        query.status = "Approved"
        query.save()
        messages.success(request,"Approved Query successfully")
        approval_mail(query)
        return redirect("portal")
    else:
        messages.error(request,"Error Processing Request")
        return redirect("query_detail_view",pk = pk,slug = slug)
@login_required
@user_passes_test(lambda user:user.profile.department != 'Unauthorized' or user.profile.department != 'Unauthorized')
def reject_query(request,pk,slug):
    query = Query.objects.get(id = pk,slug = slug)
    if request.method == "POST" and is_program_representative(request.user):
        query.status = "Rejected"
        query.save()
        messages.success(request,"Rejected Query successfully")
        rejection_mail(query)
        return redirect("portal")
    else:
        messages.error(request,"Error Processing Request")
        return redirect("query_detail_view",pk = pk,slug = slug)
@login_required
def profile(request,slug):
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance = request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            if not request.user.profile.department:
                profile_form_copy = profile_form.save(commit = False)
                if email_checker(request.user.email):
                    organization = email_parser(request.user.email)
                    if organization == 'vitstudent.ac.in':
                        profile_form_copy.role = 'Student'
                        department = Department.objects.get(departmentId = department_finder(request.user.last_name))
                        admitted_year = admitted_year_finder(request.user.last_name)
                        profile_form_copy.department = department
                        profile_form_copy.admitted_year = admitted_year
                    else:
                        profile_form_copy.role = 'Head of Department'
                else:
                    profile_form_copy.role = 'Unauthorized'
                    profile_form_copy.department = Department.objects.get(department_name = "Unauthorized")
                user_form.save()
                profile_form_copy.save()
            else:
                user_form.save()
                profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile',slug = request.user.profile.slug)
        else:
            return render(request, 'account/profile.html', {'user_form':user_form,'profile_form':profile_form,'user_form_errors':user_form.errors,'profile_form_errors':profile_form.errors})
    else:
        user_form = UserForm(instance = request.user)
        profile_form = ProfileForm(instance = request.user.profile)
        return render(request,'account/profile.html',{'user_form':user_form,'profile_form':profile_form})
@login_required
@user_passes_test(lambda user:user.profile.department != 'Unauthorized' or user.profile.department != 'Unauthorized')
def view_all_queries(request):
    program_representative = None
    if is_program_representative(request.user):
        queries = QueryFilter(request.GET,queryset = Query.objects.all().order_by('-date_of_creation'))
        pending_count = Query.objects.filter(status = "Pending Approval").count()
        approved_count = Query.objects.filter(status = "Approved").count()
        rejected_count = Query.objects.filter(status = "Rejected").count()
    else:
        queries = QueryFilter(request.GET,queryset = Query.objects.filter(user = request.user).order_by('-date_of_creation'))
        
        pending_count = Query.objects.filter(status = "Pending Approval",user = request.user).count()
        approved_count = Query.objects.filter(status = "Approved",user = request.user).count()
        rejected_count = Query.objects.filter(status = "Rejected",user = request.user).count()
    return render(request,'services/view_all_queries.html',{"Queries":queries,"Pending_Count":pending_count,"Approved_Count":approved_count,"Rejected_Count":rejected_count,})