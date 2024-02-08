from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.forms import *


class TemplateHtml(TemplateView):
    template_name='TemplateHtml.html'
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Bharat'
        ECDO['status']='single'
        return ECDO
    



class InsertSchoolByTV(TemplateView):
    template_name='InsertSchoolByTV.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByTV is done')
        



class InsertSchoolByFV(FormView):
    template_name='InsertSchoolByFV.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertSchoolByFV is done')
