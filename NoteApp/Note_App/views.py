from django.forms import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NoteForm
from .models import Note
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
    model = Note
    template_name = 'home.html'
    ordering= ['-date_created']


class DetailView(DetailView):
    model = Note
    template_name = 'DetailView.html'


class AddView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'AddView.html'
    #fields = '__all__'


class UpdateNoteView(UpdateView):
    model = Note
    template_name = 'UpdateView.html'
    fields = ['title', 'Description', 'body']


class DeleteView(DeleteView):
    model = Note
    template_name = 'DeleteView.html'
    success_url = reverse_lazy('home')
    