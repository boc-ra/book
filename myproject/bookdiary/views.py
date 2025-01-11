from django.forms import BaseModelForm
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import CustomUser
from dotenv import load_dotenv
from .models import Bookdiary
from .forms import BookdiaryForm

import os
import random
import requests


load_dotenv()

def get_random_books(api_key):
    categories = ['fiction', 'nonfiction', 'mystery', 'fantasy', 'science', 'history']
    books = []
    
    for _ in range(10):
        category = random.choice(categories)
        url = f'https://www.googleapis.com/books/v1/volumes?q=subject:{category}&langRestrict=ja&key={api_key}'
        response = requests.get(url)
        category_books = response.json().get('items', [])
        if category_books:
            books.append(random.choice(category_books))
    
    return books
class OwnerOnly(UserPassesTestMixin):
    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user

# @method_decorator(cache_page(60 * 15), name='dispatch')
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_key = os.getenv('GOOGLE_BOOKS_API_KEY')
        context['random_books'] = get_random_books(api_key)
        return context

class BookdiaryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookdiary_create.html'
    form_class = BookdiaryForm
    success_url = reverse_lazy('bookdiary:bookdiary_create_complete')
    
    def form_valid(self, form):
        '''
        フォーム保存時にログインユーザをモデルに保存
        '''
        object = form.save(commit=False) 
        object.user = self.request.user 
        object.save() 
        return super().form_valid(form) 

class BookdiaryCreateCompleteView(LoginRequiredMixin, TemplateView):
    template_name = 'bookdiary_create_complete.html'

class BookdiaryListView(LoginRequiredMixin, ListView):
    template_name = 'bookdiary_list.html'
    model = Bookdiary
    
    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        queryset = queryset.filter(user=current_user)
        
        search_type = self.request.GET.get('search_type')
        search_query = self.request.GET.get('search_query')

        if search_type and search_query:
            if search_type == 'title':
                queryset = queryset.filter(title__icontains=search_query)
            elif search_type == 'writer':
                queryset = queryset.filter(writer__icontains=search_query)
        
        return queryset.order_by("created_at")
    

class BookdiaryDetailView(LoginRequiredMixin, OwnerOnly, DetailView):
    template_name = 'bookdiary_detail.html'
    model = Bookdiary

class BookDiaryUpdateView(LoginRequiredMixin, OwnerOnly, UpdateView):
    template_name = 'bookdiary_update.html'
    model = Bookdiary
    fields = ('date', 'title','writer', 'text',)
    success_url = reverse_lazy('bookdiary:bookdiary_list')

    def form_valid(self, form):
        bookdiary = form.save(commit=False)
        bookdiary.updated_at = timezone.now()
        bookdiary.save()
        return super().form_valid(form)

class BookdiaryDeleteView(LoginRequiredMixin, OwnerOnly, DeleteView):
    template_name = 'bookdiary_delete.html'
    model = Bookdiary
    success_url = reverse_lazy('bookdiary:bookdiary_list')

