from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
# Create your views here.
from .models import Cours
from .forms import CoursForm
from django.urls import reverse

class CoursListView(ListView):
    template_name = 'cours/cours_list.html'
    queryset = Cours.objects.all()

class CoursDetailView(DetailView):
    template_name = 'cours/cours_detail.html'
    queryset = Cours.objects.all()

class CoursCreateView(CreateView):
    form_class = CoursForm
    template_name = 'cours/cours_create.html'
    queryset = Cours.objects.all()

    def form_valid(self, form):
        nom = form.cleaned_data.get('nom')
        if nom != 'français':
            form.add_error('nom', "ce cours n'est pas autorisé; validation en vue")
            return self.form_invalid(form)
        return super().form_valid(form)

class CoursUpdateView(UpdateView):
    form_class = CoursForm
    template_name = 'cours/cours_update.html'
    queryset = Cours.objects.all()

class CoursDeleteView(DeleteView):
    template_name = 'cours/cours_delete.html'
    queryset = Cours.objects.all()
    # success_url = 'cours/list/'

    def get_success_url(self):
        return reverse("cours:cours-list")