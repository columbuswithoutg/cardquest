from django.contrib import admin
from django.urls import path
from cardquest import views
from cardquest.views import HomePageView, TrainerList, PokemonCardList, CollectionList
from cardquest.views import TrainerCreateView, TrainerUpdateView, TrainerDeleteView
from cardquest.views import PokemonCardCreateView, PokemonCardUpdateView, PokemonCardDeleteView
from cardquest.views import CollectionCreateView, CollectionUpdateView, CollectionDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
    path('pokemoncard_list', PokemonCardList.as_view(), name='pokemoncard-list'),
    path('collection_list', CollectionList.as_view(), name='collection-list'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete',TrainerDeleteView.as_view(), name='trainer-delete'),
    path('pokemoncard_list/add', PokemonCardCreateView.as_view(), name='pokemoncard-add'),
    path('pokemoncard_list/<pk>', PokemonCardUpdateView.as_view(), name='pokemoncard-update'),
    path('pokemoncard_list/<pk>/delete',PokemonCardDeleteView.as_view(), name='pokemoncard-delete'),
    path('collection_list/add', CollectionCreateView.as_view(), name='collection-add'),
    path('collection_list/<pk>', CollectionUpdateView.as_view(), name='collection-update'),
    path('collection_list/<pk>/delete',CollectionDeleteView.as_view(), name='collection-delete')
]