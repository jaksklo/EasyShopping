from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from . import models
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
# Create your views here.


class ESSignUp(CreateView):
    form_class = forms.ESUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class ESDetail(LoginRequiredMixin, DetailView):
    model = models.ESUser
    template_name = 'accounts/user_detail.html'


class ESUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ESUser
    form_class = forms.ESUserCreationForm
    redirect_field_name = 'accounts/user_detail.html'
    # success_url = reverse_lazy('accounts:userdetails', kwargs={'pk': self.user.pk})
    template_name = 'accounts/edit_user.html'




class ESDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ESUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete_user.html'
