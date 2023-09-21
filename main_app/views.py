import uuid
import boto3
import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe, Review, Bid, Photo   
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ReviewForm, BidForm

# Create your views here.
class Home(ListView):
   model = Shoe
   template_name = 'home.html'
   context_object_name = 'shoes'

def about(request):
  return render(request, 'about.html')

def search_shoes(request):
   if request.method == "POST":
      searched = request.POST['searched']
      shoes = Shoe.objects.filter(name__icontains=searched)
      return render(request, 'shoes/search_shoes.html', {'searched':searched, 'shoes':shoes})
   else: 
      return render(request, 'shoes/search_shoes.html', {})

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
        # shoe = self.object
        # id_list = shoe.products.all().values_list('id')
        # unrelated_products = Product.objects.exclude(id__in=id_list)
        context['review_form'] = ReviewForm()
        context['bid_form'] = BidForm()
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

   def get_form(self, form_class=None):
      form = super().get_form(form_class)
      form.fields['size'].initial = self.object.size
      return form

class ShoeDelete(DeleteView):
   model = Shoe
   success_url = '/shoes'

@login_required
def add_review(request, shoe_id):
   form = ReviewForm(request.POST)
   if form.is_valid():
        new_review = form.save(commit=False)
        new_review.shoe_id = shoe_id
        new_review.user = request.user
        new_review.save()
   return redirect('detail', pk=shoe_id)

@login_required
def delete_review(request, shoe_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('detail', pk=shoe_id)
    
@login_required
def add_bid(request, shoe_id):
   form = BidForm(request.POST)
   if form.is_valid():
      new_bid = form.save(commit=False)
      new_bid.shoe_id = shoe_id
      new_bid.user = request.user
      new_bid.save()
   return redirect('detail', pk=shoe_id)

@login_required
def delete_bid(request, shoe_id, bid_id):
   bid = get_object_or_404(Bid, pk=bid_id)
   bid.delete()
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

def add_photo(request, shoe_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, shoe_id=shoe_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', pk=shoe_id)
