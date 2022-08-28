from Views import PokemonView
from PokemonService import PokemonService

class Pokegoshi:

    def game():
        
        escolha_usuario = PokemonView.menuUser(PokemonView)

        if escolha_usuario == '1': 
            escolha_pokemon = PokemonView.menuPokemon(PokemonView)
        elif escolha_usuario  == '2':
            print('\nPrograma Encerrado\n')
            print("="*70)

        mascote = PokemonService.get_data(escolha_pokemon)

        PokemonView.mascoteView(mascote)

        PokemonView.sucessoAdocao()