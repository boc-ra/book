
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Bookdiary
from .forms import BookdiaryForm


class IndexView(TemplateView):
    template_name = 'index.html'

class BookdiaryCreateView(CreateView):
    template_name = 'bookdiary_create.html'
    form_class = BookdiaryForm
    success_url = reverse_lazy('bookdiary:bookdiary_create_complete')

class BookdiaryCreateCompleteView(TemplateView):
    template_name = 'bookdiary_create_complete.html'

class BookdiaryiaryListView(ListView):
    template_name = 'bookdiary_list.html'
    model = Bookdiary

class BookdiaryDetailView(DetailView):
    template_name = 'bookdiary_detail.html'
    model = Bookdiary

class BookDiaryUpdateView(UpdateView):
    template_name = 'bookdiary_update.html'
    model = Bookdiary
    fields = ('date', 'title','writer', 'text',)
    success_url = reverse_lazy('bookdiary:bookdiary_list')

    def form_valid(self, form):
        bookdiary = form.save(commit=False)
        bookdiary.updated_at = timezone.now()
        bookdiary.save()
        return super().form_valid(form)

class BookdiaryDeleteView(DeleteView):
    template_name = 'bookdiary_delete.html'
    model = Bookdiary
    success_url = reverse_lazy('bookdiary:bookdiary_list')

