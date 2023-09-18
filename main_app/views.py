from django.shortcuts import render, redirect
from .models import Shoe
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class ShoeList(LoginRequiredMixin, ListView):
    model = Shoe
    template_name = 'shoes/index.html'
    context_object_name = 'shoes'

    def get_queryset(self):
       return Shoe.objects.filter(user=self.request.user)
    
class ShoeDetail(LoginRequiredMixin, DetailView):
    model = Shoe
    template_name = 'shoes/detail.html'
    context_object_name = 'shoe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shoe = self.object
        # id_list = shoe.products.all().values_list('id')
        # unrelated_products = Product.objects.exclude(id__in=id_list)
        context['review_form'] = ReviewForm()
        # context['products'] = unrelated_products
        return context
    
class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = ['name', 'brand', 'size', 'colorway', 'description', 'release_date', 'price']
    success_url = '/shoes'

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)
    
class ShoeUpdate(UpdateView):
   model = Shoe
   fields = ['name', 'brand', 'size', 'colorway', 'description', 'release_date', 'price']


class ShoeDelete(DeleteView):
   model = Shoe
   success_url = '/shoes'

@login_required
def add_review(request, shoe_id):
   form = ReviewForm(request.POST)
   if form.is_valid():
        new_review = form.save(commit=False)
        new_review.shoe_id = shoe_id
        new_review.save()
   return redirect('detail', pk=shoe_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

