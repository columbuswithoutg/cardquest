from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer, Collection
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from cardquest.forms import TrainerForm, PokemonCardForm, CollectionForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = "trainer.html"
    paginate_by = 15

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemon-card.html"
    paginate_by = 15

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = "collection.html"
    paginate_by = 15

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer/trainer_add.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer/trainer_edit.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer/trainer_del.html'
    success_url = reverse_lazy('trainer-list')

class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokecard/pokemoncard_add.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokecard/pokemoncard_edit.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokecard/pokemoncard_del.html'
    success_url = reverse_lazy('pokemoncard-list')

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_add.html'
    success_url = reverse_lazy('collection-list')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_edit.html'
    success_url = reverse_lazy('collection-list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection/collection_del.html'
    success_url = reverse_lazy('collection-list')