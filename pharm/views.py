from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from .models import *
from .forms import *
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


@login_required
def index(request):
    if request.user.is_pharmacist:
        return render(request, 'pharm/pharmacist/home.html')
    # if request.user.is_patient:
    #     return render(request, 'pharm/patient/homepage.html')
    return render(request, 'pharm/logout.html')


class HomeView(View):
    template_name = 'pharm/home.html'
    

    def get(self,request):
        products = Product.objects.all()
        ctx = {
            'products': products
        }
        return render(request,self.template_name,ctx)


class PhHome(LoginRequiredMixin,View):
    template_name = 'pharm/pharmacist/home.html'
    

    def get(self,request,pk=None):
        return render(request,self.template_name)


class AddProduct(LoginRequiredMixin,View):
    template_name = 'pharm/pharmacist/add_product.html'
    success_url = 'pharm/pharmacist/home.html'

    def get(self,request,pk):
        form = AddProduct()
        ctx = {'form':form}
        return render(request,self.template_name,ctx)

    def post(self,request,pk):
        return render(request,self.success_url)

