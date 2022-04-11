from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.shortcuts import render
from shoppingList.models import ShoppingList

User = get_user_model()

class HomeView(TemplateView):
    template_name = "index.html"

    def get(self,request):
        user_count = User.objects.count()
        lists_count = ShoppingList.objects.count()
        context = {"user_count": user_count,
                   "lists_count": lists_count}
        return render(request, self.template_name, context)


class AfterLogoutView(TemplateView):
    template_name = 'thanks.html'
