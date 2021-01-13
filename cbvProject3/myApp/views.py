from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from myApp.models import HOD
from django.urls import reverse_lazy
class HODListView(ListView):
      model=HOD
class HODDetailView(DetailView):
      model=HOD
class HODCreateView(CreateView):
      model=HOD
      fields='__all__'
class HODUpdateView(UpdateView):
      model=HOD
      fields=('name','sal')
class HODDeleteView(DeleteView):
      model=HOD
      success_url=reverse_lazy('hods')
