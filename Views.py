class PokemonView:

    def menuUser(self):

        print()
        print("="*70)
        print("#"*23, "BEM VINDO AO POKEGOSHI", "#"*23)
        print("="*70)
        
        nome_usuario = str(input("\nQual é o seu nome: ")).capitalize()
        print()
        print("="*70)
        
        print(f"\n{nome_usuario} Você deseja:")

        print('''
            [1] Adotar mascote virtual
            [2] Sair\n''')

        escolha_usuario = str(input("Escolha uma das opções [1] [2]: "))
        print()

        while escolha_usuario not in "12":
            escolha_usuario = str(input("Favor escolher uma das seguintes opções [1] [2]: "))
        print("="*70)

        return escolha_usuario

    def menuPokemon(self):
        
        print("\nEscolha um Pokemon da Lista Abaixo:")

        print('''
            [1] Bulbasaur
            [2] Charmander
            [3] Squirtle
            [4] Nidoran-m
            [5] Nidoran-f\n''')

        print("="*70, "\n")

        escolha_pokemon = str(input("Escolha uma das opções [1] [2] [3] [4] [5]: "))
        print()
        while escolha_pokemon not in "12345":
            escolha_pokemon = str(input("Favor escolher uma das seguintes opções [1] [2] [3] [4] [5]: "))
        print("="*70)

        if escolha_pokemon == "1":
            escolha_pokemon = "1"

        elif escolha_pokemon == "2":
            escolha_pokemon = "4"

        elif escolha_pokemon == "3":
            escolha_pokemon = "7"

        elif escolha_pokemon == "4":
            escolha_pokemon = "32"

        elif escolha_pokemon == "5":
            escolha_pokemon = "29"

        return escolha_pokemon

    def mascoteView(mascote):       
        print('\nVocê escolheu: ')
        print(f'''
            Nome do Pokemon: {mascote._nome}
            ID do Pokemon: {mascote._id_pokemon}
            Altura: {mascote._altura}
            Peso: {mascote._peso}
            
            Habilidades: {mascote._habilidades}\n''')
        print("="*70)

    def sucessoAdocao():
        print('\nADOÇÃO CONCLUÍDA COM SUCESSO, SEU OVO ESTÁ CHOCANDO...')
        print('''
              ███╗
             ██████╗
            ████████╗
            ████████║
            ████████║
            ╚█████╔╝
             ╚════╝\n''')
        print("="*70)
        print()