import datetime

from . import models
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import Http404
from django.urls import reverse_lazy, reverse

User = get_user_model()

# Create your views here.
class ShoppingListCreateView(CreateView,LoginRequiredMixin, SelectRelatedMixin):
    # ten widok powstał z pominięciem tworzenia formularza

    model = models.ShoppingList
    fields = ('title', 'products')
    template_name = 'shoppingList/create.html'

    labels = {
        'products': 'Please type comma-separated list of products'
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UserShoppingLists(ListView):
    model = models.ShoppingList
    template_name = 'shoppingList/lists_by_user.html'
    ordering = ['+created_date']

    def get_queryset(self):
        try:
            self.list_user = User.objects.prefetch_related('shoplists').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.list_user.shoplists.all().order_by('-created_date')

    # nadpisanie tej metody pozwala dodać ekstra informacje do widoku listy
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_user'] = self.list_user
        return context


class ShoppingListDetailView(SelectRelatedMixin, DetailView):
    model = models.ShoppingList
    template_name = 'shoppingList/list_detail.html'
    select_related = ('author',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author__username__iexact=self.kwargs.get("username"))


class ShoppingListUpdateView(UpdateView,SelectRelatedMixin):
    model = models.ShoppingList

    fields = ('title', 'products')
    template_name = 'shoppingList/edit_list.html'
    redirect_field_name = 'shoppingList/list_detail.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.edit_date = datetime.datetime.now()
        self.object.save()
        return super().form_valid(form)


class ShoppingListDeleteView(DeleteView, SelectRelatedMixin):
    model = models.ShoppingList
    template_name = 'shoppingList/list_confirm_delete.html'
    # success_url = reverse_lazy('shoplists:listsbyuser', kwargs={'username': User.username})
    select_related = ('author',)

    def delete(self, request, *args, **kwargs):
        # the Post object
        self.object = self.get_object()
        if self.object.User == request.user:
            success_url = self.get_success_url()
            self.object.delete()
        #     return http.HttpResponseRedirect(success_url)
        # else:
        #     return http.HttpResponseForbidden("Cannot delete other's posts")

    def get_success_url(self):
        return reverse('shoplists:listsbyuser', kwargs={'username': self.object.author.username})
