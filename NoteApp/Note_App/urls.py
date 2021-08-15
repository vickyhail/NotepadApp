from django.urls import path
from .views import HomeView, DetailView, AddView, UpdateNoteView, DeleteView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('note/<int:pk>', DetailView.as_view(), name='detail'),
    path('addnote/', AddView.as_view(), name='add'),
    path('editnote/<int:pk>', UpdateNoteView.as_view(), name='update'),
    path('deletenote/<int:pk>', DeleteView.as_view(), name='delete'),


    
] 
