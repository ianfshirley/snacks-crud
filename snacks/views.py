from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snacks"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = "__all__"


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name", "purchaser", "description"] # "__all__" for all of them


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")



