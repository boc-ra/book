from django.urls import path
from . import views

app_name = 'bookdiary'
urlpatterns = [
    path('home/', views.IndexView.as_view(), name='index'),
    path('bookdiary/create/', views.BookdiaryCreateView.as_view(), name='bookdiary_create'),
    path('bookdiary/create/complete/', views.BookdiaryCreateCompleteView.as_view(), name='bookdiary_create_complete'),
    path('bookdiary/list/', views.BookdiaryListView.as_view(), name='bookdiary_list'),
    path('bookdiary/detail/<uuid:pk>/', views.BookdiaryDetailView.as_view(), name='bookdiary_detail'),
    path('bookdiary/update/<uuid:pk>/', views.BookDiaryUpdateView.as_view(), name='bookdiary_update'),
    path('bookdiary/delete/<uuid:pk>/', views.BookdiaryDeleteView.as_view(), name='bookdiary_delete'),
]