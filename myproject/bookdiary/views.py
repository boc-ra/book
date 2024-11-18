from django.forms import BaseModelForm
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import CustomUser

from .models import Bookdiary
from .forms import BookdiaryForm

class OwnerOnly(UserPassesTestMixin):
    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

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
        current_user = self.request.user.username # ログイン中のユーザ名を取得（CustomUserモデルのusernameレコードの値を取得）
        user_data = CustomUser.objects.get(username=current_user) # QuerySet(条件が一致するレコードを全て取得)
        if user_data:
            queryset = Bookdiary.objects.filter(user=user_data).all() # QuerySet（一致するレコード全て取得）
            queryset = queryset.order_by("created_at")
        return queryset
    

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

