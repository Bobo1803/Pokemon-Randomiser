import random
import time

from test import testing

# add function to make certain pokemon unobtainable after getting a related one (cant get hitmonlee in gen 1 after getting hitmonchan, choosing betweeen fossils etc etc)


# add function for legendary toggle (also ultra beasts)
# add function for evolutions on or off
# add function to check if player has access to trade evos
#add function for postgame mons
# (list).remove to remove elements when user picks to use these functions
# maybe remove mons based on version exclusivity??
# Remove any pre evoloutions if turned off, but if player is unable to use trade evos, add back the stage before the final evo back
##make exceptions for certain games, for example, in yellow ver starter pikachu cant evolve so re add it into gen 1 pre evo list
#add ability to remove post game mons (mewtwo in gen 1 for example)
#remove starters after picking
#account for HM users. Probably do that later because it will be VERY HARD
#function to allow for a starter to be chosen (do this twice for x and y)
#add function to decide wheather to allow baby pokemon
#maybe have a function to turn off pokemon that can only be obtained if bred as they are obtained at very low level

### lists of removeable items

####removals to make based on game events:
#Kanto fossils
#Hoenn fossils
#fighting dojo mons
#eeveeloutions kanto
#make porygon optional becuase it is quite out of reach
#postgame pokemon like mewtwo can be turned off

#gen 2 ninetales, arcanine, flareon (fire stone)
#gen 2 poliwrath, cloyster , starmie , vaporeon (water stone)
#gen 2 raichu, jolteon (thunderstone)
#gen 2 vileplume, vixtreebel, exeggutor (leaf stone
#gen 2 check if baby pokemon obtained from the egg are able to be caught if the egg doesnt have them

#gen 3 huntail or gorebyss
#gen 3 lileep/cradily, anorith/armaldo dossils
#gen 3 wigglytuff, delcatty (moon stone)(RUBY SAPHIRE ONLY)
# latias/latios (may want to make a post game exception

#gen 3 frlg eevee choice


#gen 4 in platinum, caranidos and sheildon availability is decided by ID number, need to find soloution as this is arkward

#gen 4 hgss

#gen 5 fossils tirtouga/carracosta, archen/archeops

#gen 5 bw2, yancy and curtis trades depend on player gender. meowth/mankey, teddurisa/phanphy mawhile/sableye, shellos

#gen 6 remember that you can also get kanto starters
#gen 6 tyrunt/tyrantrum, amaura/aurorus
#gen 6 gen 1 legendary bird trio is here based on starter pick but it is based on postgame

#gen 6 oras fossils again

#gen 7 only mutual exclusives are starters

#gen 8 urshifu forms, work out how to handle this later. how will dlc work??
#gen 8 glastrier and spectrier plus regieleki and regidrago

#gen 9 starters only

#XD (maybe do this game) only one eeveeloution is available
#XD fire stone evos ninetales, arcanine, flareon
#XD leaf stones evos victreebel, shiftry







legends = ["Mewtwo", "Zapdos", "Moltres", "Articuno", "Ho-oh", "Lugia", "Suicune", "Raikou", "Entei", "Rayquazza",
           "Kyogre", "Groundon", "Latias", "Latios", "Regice", "Regirock", "Registeel", "Palkia", "Dialga", "Uxie",
           "Azelf", "Mesprit", "Giritina", "Cresselia", "Regigigas", "Heatran", "Zekrom", "Reshiram", "Kyurem",
           "Coballion", "Terrakion", "Verizion", "Landorous", "Thundurus", "Tornadus", "Xerneas", "Yveltal", "Zygarde",
           "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Necrozma", "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini",
           "Zacian", "Zamazenta", "Eternatus", "Silvally", "Type-Null", "Urshifu", "Kubfu", "Calyrex", "Regieleki",
           "Regidrago", "Glastrier", "Spectrier", "Miraidon", "Koraidon", "Ting-Lu", "Chien-Pau", "Chi-Yu", "Wo-Chien",
           "Enamorous"]
ultraBeasts = ["Nihelego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Poipole",
               "Naganadel", "Stakataka", "Blacephalon"]
tradeEvos = ["Politoed", "Alakazam", "Machamp", "Golem", "Slowking", "Gengar", "Steelix", "Rhyperior", "Kingdra",
             "Scizor", "Electivire", "Magmortar", "Porygon2", "PorygonZ", "Milotic", "Dusknoir", "Huntail", "Gorebyss",
             "Gigalith", "Conkeldurr", "Escavalier", "Accelgor", "Aromatisse", "Slurpuff", "Trevenant", "Gourgeist"]
preEvosGen1 = ["Bulbasaur", "Ivysaur", "Charmander", "Charmeleon", "Squirtle", "Wartortle", "Weedle", "Kakuna",
               "Caterpie", "Metapod", "Pidgey", "Pidgeotto", "Rattata", "Ekans", "Meowth"
               "Spearow", "Pikachu", "Sandshrew", "Nidoran F", "Nidorina", "Nidoran M",
               "Nidorino", "Clefairy", "Vulpix", "Jigglypuff", "Zubat",
               "Oddish", "Gloom", "Paras", "Venonat", "Diglett",
               "Psyduck", "Mankey", "Growlithe", "Poliwag", "Poliwhirl", "Abra", "Kadabra", "Machop", "Machoke",
               "Bellsrpout", "Weepinbell", "Tentacool", "Geodude", "Graveler", "Ponyta", "Koffing",
               "Slowpoke", "Magnemite", "Doduo", "Seel", "Grimer", "Shellder",
               "Gastly", "Haunter", "Drowzee", "Krabby", "Voltorb", "Exeggcute", "Cubone",
               "Rhyhorn", "Horsea", "Goldeen", "Staryu",
               "Majikarp", "Eevee", "Omanyte", "Kabuto",
               "Dratini", "Dragonair"]

preEvosGen2 =  ["Chikorita", "Bayleef", "Cyndaquill", "Quilava", "Totodile", "Croconaw", "Pidgey", "Pidgeotto",
            "Spearow", "Hoothoot", "Rattata",  "Sentret","Pichu", "Pikachu", "Caterpie", "Metapod",
            "Weedle", "Kakuna", "Ledyba", "Geodude", "Graveler",  "Zubat", "Golbat", "Cleffa", "Clefairy",
             "Jigglypuff", "Igglybuff", "Togepi", "Sandshrew", "Ekans", "Dunsparce", "Mareep", "Flaafy", "Wooper",
             "Ghastly", "Haunter", "Unown", "Onix", "Bellsprout", "Weepinbell", "Hoppip", "Skiploom", "Paras",
            "Poliwag", "Poliwhirl", "Majikarp", "Goldeen", "Slowpoke", "Oddish", "Gloom",
             "Bellossom", "Drowzee", "Abra", "Kadabra" , "Ditto", "Pineco", "Nidoran F", "Nidorina", "Nidoran M",
            "Nidorino",  "Yanma", "Sunkern", "Exeggcute",  "Sudowoodo", "Wobbuffet", "Venonat",  "Scyther",
            "Pinsir", "Heracross", "Koffing",  "Grimer", "Magnemite", "Voltorb", "Aipom",  "Snubbul",
            "Vulpix", "Stantler", "Marill", "Diglett", "Meowth", "Psyduck",
            "Machop", "Machoke", "Tyrogue", "Girafarig", "Tauros", "Miltank", "Magby","Smoochum", "Elekid",
            "Mr Mime", "Smeargle", "Farfetch'd", "Natu", "Qwilfish", "Tentacool", "Krabby", "Shuckle", "Staryu", "Shellder",
             "Corsola", "Remoraid","Chinchou", "Seel", "Lickitung", "Tangela", "Eevee",
            "Horsea", "Seadra", "Delibird" , "Swinub", "Phanphy", "Skarmory", "Doduo", "Ponyta",
            "Cubone", "Kangaskhan", "Rhyhorn", "Murkrow", "Houndour", "Slugma", "Sneasel", "Misdreavus", "Porygon", "Chansey",
             "Lapras", "Aerodactyl", "Snorlax",
             "Raikou", "Entei", "Suicune", "Dratini", "Dragonair", "Larvitar", "Pupitar", "Lugia", "Ho-oh"]

# lists of pokemon for each game

Ymons = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle",
         "Blastoise", "Caterpie", "Metapod", "Butterfree", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate",
         "Spearow", "Fearow", "Pikachu", "Sandshrew", "Sandslash", "Nidoran F", "Nidorina", "Nidoqueen", "Nidoran M",
         "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Nintetales", "Jigglypuff", "Wigglytuff", "Zubat",
         "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio",
         "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath",
         "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp",
         "Bellsrpout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta",
         "Rapidash",
         "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer",
         "Muk", "Shellder", "Cloyster",
         "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode",
         "Exeggcute", "Exeggutor", "Cubone", "Marowak",
         "Hitmonlee", "Hitmonchan", "Lickitung", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea",
         "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
         "Mr.Mime", "Scyther", "Pinsir", "Tauros", "Majikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon",
         "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto",
         "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
         "Mewtwo"]

Rmons = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle",
         "Blastoise","Weedle", "Kakuna", "Beedrill", "Caterpie", "Metapod", "Butterfree", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate",
         "Ekans", "Arbok", "Spearow", "Fearow", "Pikachu", "Raichu", "Nidoran F", "Nidorina", "Nidoqueen", "Nidoran M",
         "Nidorino", "Nidoking", "Clefairy", "Clefable", "Jigglypuff", "Wigglytuff", "Zubat",
         "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio",
         "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath",
         "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta",
         "Rapidash",
         "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer",
         "Muk", "Shellder", "Cloyster",
         "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Koffing", "Weezing"
         "Exeggcute", "Exeggutor", "Cubone", "Marowak",
         "Hitmonlee", "Hitmonchan", "Lickitung", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea",
         "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
         "Mr.Mime", "Scyther", "Jynx", "Electabuzz", "Tauros", "Majikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon",
         "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto",
         "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
         "Mewtwo"]

Bmons = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle",
         "Blastoise","Weedle", "Kakuna", "Beedrill", "Caterpie", "Metapod", "Butterfree", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate",
          "Spearow", "Fearow", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran F", "Nidorina", "Nidoqueen", "Nidoran M",
         "Nidorino", "Nidoking", "Clefairy", "Clefable", "Jigglypuff", "Wigglytuff", "Zubat",
         "Golbat", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian"
         "Psyduck", "Golduck", "Poliwag", "Poliwhirl", "Poliwrath",
         "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta",
         "Rapidash", "Bellsprout", "Weepinbell", "Victreebel"
         "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer",
         "Muk", "Shellder", "Cloyster",
         "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Koffing", "Weezing",
         "Exeggcute", "Exeggutor", "Cubone", "Marowak",
         "Hitmonlee", "Hitmonchan", "Lickitung", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea",
         "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
         "Mr.Mime","Magmar", "Jynx","Pinsir", "Tauros", "Majikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon",
         "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto",
         "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
         "Mewtwo"]

goldMons = ["Chikorita", "Bayleef", "Meganium", "Cyndaquill", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Pidgey", "Pidgeotto", "Pidgeot",
            "Spearow", "Fearow", "Hoothoot", "Noctowl", "Rattata", "Raticate", "Sentret", "Furret", "Pichu", "Pikachu", "Raichu", "Caterpie", "Metapod", "Butterfree",
            "Weedle", "Kakuna", "Beedrill", "Spinarak", "Ariados", "Geodude", "Graveler", "Golem", "Zubat", "Golbat", "Crobat", "Cleffa", "Clefairy",
            "Clefable", "Jigglypuff", "Igglybuff","Wigglytuff", "Togepi", "Togetic", "Sandshrew", "Sandslash", "Ekans", "Arbok", "Dunsparce", "Mareep", "Flaafy", "Ampharos", "Wooper",
            "Quagsire", "Ghastly", "Haunter", "Gengar", "Unown", "Onix", "Steelix", "Bellsprout", "Weepinbell", "Victreebel", "Hoppip", "Skiploom", "Jumpluff", "Paras",
            "Parasect", "Poliwag", "Poliwhirl", "Poliwrath", "Politoed", "Majikarp", "Gyarados", "Goldeen", "Seaking", "Slowpoke", "Slowbro", "Slowking", "Oddish", "Gloom",
            "Vileplume", "Bellossom", "Drowzee", "Hypno", "Abra", "Kadabra" , "Alakazam", "Ditto", "Pineco", "Forretress", "Nidoran F", "Nidorina", "Nidoqueen", "Nidoran M",
            "Nidorino", "Nidoking", "Yanma", "Sunkern", "Sunflora", "Exeggcute", "Exeggutor", "Sudowoodo", "Wobbuffet", "Venonat", "Venomoth", "Scyther", "Scizor",
            "Pinsir", "Heracross", "Koffing", "Weezing", "Grimer", "Muk", "Magnemite", "Magneton", "Voltorb", "Electrode", "Aipom", "Ambipom", "Snubbul", "Granbull",
             "Growlithe", "Arcanine", "Stantler", "Marill", "Azumarill", "Diglett", "Dugtrio", "Mankey", "Primeape", "Golduck", "Psyduck",
            "Machop", "Machoke", "Machamp", "Tyrogue", "Hitmonlee", "Hitmonchan", "Hitmontop", "Girafarig", "Tauros", "Miltank", "Magby", "Magmar", "Smoochum", "Jynx", "Elekid",
            "Electabuzz", "Mr Mime", "Smeargle", "Farfetch'd", "Natu", "Xatu", "Qwilfish", "Tentacool", "Tentacruel", "Krabby", "Kingler", "Shuckle", "Staryu", "Starmie", "Shellder",
            "Cloyster", "Corsola", "Remoraid", "Octillery", "Chinchou", "Lanturn", "Seel", "Dewgong", "Lickitung", "Tangela", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon",
            "Horsea", "Seadra", "Kingdra", "Gligar", "Delibird" , "Swinub", "Piloswine", "Teddiursa", "Ursaring", "Mantine", "Doduo", "Dodrio", "Ponyta",
            "Rapidash", "Cubone", "Marowak", "Kangaskhan", "Rhyhorn", "Rhydon", "Murkrow", "Houndour", "Houndoom", "Slugma", "Magcargo", "Sneasel", "Misdreavus", "Porygon", "Porygon2", "Chansey",
            "Blissey", "Lapras", "Aerodactyl", "Snorlax",
             "Raikou", "Entei", "Suicune", "Dratini", "Dragonite", "Dragonair", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-oh"]

silverMons = ["Chikorita", "Bayleef", "Meganium", "Cyndaquill", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Pidgey", "Pidgeotto", "Pidgeot",
            "Spearow", "Fearow", "Hoothoot", "Noctowl", "Rattata", "Raticate", "Sentret", "Furret", "Pichu", "Pikachu", "Raichu", "Caterpie", "Metapod", "Butterfree",
            "Weedle", "Kakuna", "Beedrill", "Ledyba", "Ledian", "Geodude", "Graveler", "Golem", "Zubat", "Golbat", "Crobat", "Cleffa", "Clefairy",
            "Clefable", "Jigglypuff", "Igglybuff", "Wigglytuff", "Togepi", "Togetic", "Sandshrew", "Sandslash", "Ekans", "Arbok", "Dunsparce", "Mareep", "Flaafy", "Ampharos", "Wooper",
            "Quagsire", "Ghastly", "Haunter", "Gengar", "Unown", "Onix", "Steelix", "Bellsprout", "Weepinbell", "Victreebel", "Hoppip", "Skiploom", "Jumpluff", "Paras",
            "Parasect", "Poliwag", "Poliwhirl", "Poliwrath", "Politoed", "Majikarp", "Gyarados", "Goldeen", "Seaking", "Slowpoke", "Slowbro", "Slowking", "Oddish", "Gloom",
            "Vileplume", "Bellossom", "Drowzee", "Hypno", "Abra", "Kadabra" , "Alakazam", "Ditto", "Pineco", "Forretress", "Nidoran F", "Nidorina", "Nidoqueen", "Nidoran M",
            "Nidorino", "Nidoking", "Yanma", "Sunkern", "Sunflora", "Exeggcute", "Exeggutor", "Sudowoodo", "Wobbuffet", "Venonat", "Venomoth", "Scyther", "Scizor",
            "Pinsir", "Heracross", "Koffing", "Weezing", "Grimer", "Muk", "Magnemite", "Magneton", "Voltorb", "Electrode", "Aipom", "Ambipom", "Snubbul", "Granbull",
            "Vulpix", "Ninetales", "Stantler", "Marill", "Azumarill", "Diglett", "Dugtrio", "Meowth", "Persian", "Golduck", "Psyduck",
            "Machop", "Machoke", "Machamp", "Tyrogue", "Hitmonlee", "Hitmonchan", "Hitmontop", "Girafarig", "Tauros", "Miltank", "Magby", "Magmar", "Smoochum", "Jynx", "Elekid",
            "Electabuzz", "Mr Mime", "Smeargle", "Farfetch'd", "Natu", "Xatu", "Qwilfish", "Tentacool", "Tentacruel", "Krabby", "Kingler", "Shuckle", "Staryu", "Starmie", "Shellder",
            "Cloyster", "Corsola", "Remoraid", "Octillery", "Chinchou", "Lanturn", "Seel", "Dewgong", "Lickitung", "Tangela", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon",
            "Horsea", "Seadra", "Kingdra", "Delibird" , "Swinub", "Piloswine", "Phanphy", "Donphan", "Skarmory", "Doduo", "Dodrio", "Ponyta",
            "Rapidash", "Cubone", "Marowak", "Kangaskhan", "Rhyhorn", "Rhydon", "Murkrow", "Houndour", "Houndoom", "Slugma", "Magcargo", "Sneasel", "Misdreavus", "Porygon", "Porygon2", "Chansey",
            "Blissey", "Lapras", "Aerodactyl", "Snorlax",
             "Raikou", "Entei", "Suicune", "Dratini", "Dragonite", "Dragonair", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-oh"]



gen1TradeEvo = ["Alakazam", "Machamp", "Golem", "Gengar"]

gen1TradePreEvos = ["Kadabra", "Machoke", "Graveler", "Haunter"]

gen1PostGameMons = ["Mewtwo"]

#starter lists to stop you from getting multiple different starters, doesnt matter in yellow version because all starters are available
ifBulbsasaur = ["Squirtle", "Wartortle","Blastoise", "Charmander", "Charmeleon", "Charizard"]
ifSquirtle = ["Bulbasuar", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard"]
ifCharmander = ["Bulbasuar", "Ivysaur", "Venusaur", "Squirtle", "Wartortle","Blastoise"]




#global function used for these functions so that lists can be editied on a global scope rather than just within a function (would be useless)
def kantoStarterList(monChoice):

    global listSelect
    if monChoice == "Squirtle" or monChoice == "Wartortle" or monChoice == "Blastoise":

        (listSelect).remove("Charmander", "Charmeleon", "Charizard", "Bulbasaur", "Ivysaur", "Venusaur")

    elif monChoice == "Bulbasaur" or monChoice == "Ivysaur" or monChoice == "Venusaur":

        (listSelect).remove("Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise")

    elif monChoice == "Charmander" or monChoice == "Charmeleon" or monChoice == "Charizard":

        (listSelect).remove("Bulbasaur", "Ivysaur", "Venusaur", "Squirtle", "Wartortle", "Blastoise")



def fightingDogoList(monChoice):
    global listSelect
    if monChoice == "Hitmonlee":

        (listSelect).remove("Hitmonchan")

    elif monChoice == "Hitmonchan":

        (listSelect).remove("Hitmonlee")

def kantoFossilsList(monChoice):

    global listSelect
    if monChoice == "Omanyte" or monChoice == "Omastar":

        if "Kabuto" in listSelect:

            (listSelect).remove("Kabuto")

        (listSelect).remove("Kabutops")

    elif monChoice == "Kabuto" or monChoice == "Kabutops":

        if "Omanyte" in listSelect:

            (listSelect).remove("Omanyte")

        (listSelect).remove("Omastar")


def eeveeListGen13(monChoice):

    global listSelect

    if monChoice == "Eevee":

        (listSelect).remove("Vaporeon")

        (listSelect).remove("Jolteon")

        (listSelect).remove("Flareon")

    elif monChoice == "Vaporeon":

        if "eevee" in listSelect:

            (listSelect).remove("Eevee")

        (listSelect).remove("Jolteon")

        (listSelect).remove("Flareon")

    elif monChoice == "Jolteon":

        if "eevee" in listSelect:

            (listSelect).remove("Eevee")

        (listSelect).remove("Vaporeon")

        (listSelect).remove("Flareon")

    elif monChoice == "Flareon":

        if "eevee" in listSelect:

            (listSelect).remove("Eevee")

        (listSelect).remove("Jolteon")

        (listSelect).remove("Vaporeon")

def gen1PorygonSelect(poryCheck):

    global listSelect

    while poryCheck == "Unspecified":

        try:


            porygonCheck = input("Do you want to allow for porygon (Can be hard to get due to 9999 coins in game corner requirement)")

            if porygonCheck == "yes" or porygonCheck == "Yes":

                poryCheck = "specified"

            elif porygonCheck == "No" or porygonCheck == "no":
                #try plus exception becuase of error that says porygon doesnt exist possibly???
                if "Porygon" in listSelect:

                    listSelect.remove("Porygon")

                poryCheck = "specified"



            else:

                print("Please enter a valid input")

        except ValueError:

            continue


#these operations to decide to include legendaries and pre evos or not dont work. they do if put in the list without being in a def functions though
def legendSelectOperation(legendSelection):

    global listSelect
    while legendSelection == "Unspecified":

        legendChoice = input("Do you want to allow legendaries?")

        if legendChoice == "yes" or legendChoice == "Yes":

            print("Legendaries are on")

            legendSelection = "specified"

        elif legendChoice == "no" or legendChoice == "No":

            print("legendaries are turned off")

            legendSelection = "specified"

            listSelect = [i for i in (listSelect) if i not in legends]







        else:
            print("invalid input")


def evoAllowSelect(evosAllowed, preEvosGenSelect, evoChoice):

    global listSelect
    while evosAllowed == "Unspecified":

        evoChoice = input("Do you want to allow pre evoloutions?")

        if evoChoice == "Yes" or evoChoice == "yes":

            print("pre evoloutions are allowed")

            evosAllowed = "Specified"

        elif evoChoice == "No" or evoChoice == "no":

            print("pre evoloutions are not allowed")

            evosAllowed = "Specified"



            listSelect2 = [l for l in listSelect if l not in preEvosGenSelect]

            listSelect = listSelect2




        else:

            print("Invalid option, please enter yes or no")

def tradeEvoOperation(tradeEvosSelection, evoChoice):

    global listSelect

    #remove using list comprehension trade evo final stage mons, then add them back in thier middle stage.
    ##PROBLEM: this approach wont really work across multiple gens, maybe make different trade evo lists per generation to apply for each game selected

    while tradeEvosSelection == "Unspecified":

            tradeEvoSelect = input("Do you have access to trade evoloutions?")

            if tradeEvoSelect == "Yes" or tradeEvoSelect == "yes":

                tradeEvosSelection = "Specified"

            elif tradeEvoSelect == "No" or tradeEvoSelect == "no":

                tradeEvosSelection = "Specified"

                listSelect = [i for i in (listSelect) if i not in gen1TradeEvo]
                #removes trade evo mons but doesnt add back their original evos. add them back if they were removed by final stage only

                if evoChoice == "No" or "no":

                    listSelect.extend(gen1TradePreEvos)


            else:

                print("Invalid input, please enter yes or no")

def teamSelectionAction(teamNoSelect, monSelect, selectCount=None):
#make a different team select action for each gen because of differing functions required
#possible index error when using this function. use error handling to sort this out (Try + except)
    global listSelect

    while teamNoSelect == "Unspecified":

        try:

            monCount = int(input("From 1-6, how many pokemon do you want in your team?"))

            if monCount in range(1, 7):
                teamNoSelect = "Specified"

                selectCount = 0

                while selectCount < monCount:

                    try:

                        monChoice = random.choice(listSelect)

                        print(monChoice)

                        (listSelect).remove(monChoice)

                        selectCount = selectCount + 1

                        fightingDogoList(monChoice)

                        eeveeListGen13(monChoice)

                        kantoFossilsList(monChoice)

                    except IndexError :

                        print("test error")





            else:

                print("invalid amount of pokemon")

        except ValueError:

            print("please enter a number between 1 and 6")

            #find way to return to the top of the try when exception is used

def gen1PostGameSelect(postGameAllowed, gameChoice, postGameList):

    global listSelect


    if gameChoice == "Yellow" or gameChoice == "yellow" or gameChoice == "1" or gameChoice == "Red" or gameChoice == "red" or gameChoice == "2" or gameChoice == "Blue" or gameChoice == "blue" or gameChoice == "3":
    #selecting which list of postgame pokemon to choose between based on which game is chosen
        postGameList = gen1PostGameMons

    postGameChoice = input("Do you want to inclube postgame pokemon?")

    while postGameAllowed == "Unspecified":

        if postGameChoice == "Yes" or postGameChoice == "yes":
            #make it so that the post game list selected changes based on which game is chosen


            listSelect = [i for i in listSelect if i in postGameList]

            postGameAllowed = "Specified"

        elif postGameChoice == "no" or postGameChoice == "No":

            postGameAllowed = "Specified"


        else:

            print("Invalid input, please enter yes or no")




def gameSelect(legends, preEvosGen1, evoChoice = None, monSelect=None, postGameList=None):

    global listSelect
    tradeEvosSelection = "Unspecified"
    teamNoSelect = "Unspecified"
    legendSelection = "Unspecified"
    evosAllowed = "Unspecified"
    postGameAllowed = "Unspecified"
    poryCheck = "Unspecified"
    gameSelection = 0
    while gameSelection == 0:
        gameChoice = input("""Enter these numbers to choose a game:
                           1.Yellow
                           2.Red
                           3.Blue
                           4.Gold
                           5.Silver
                           6.Crystal
                           7.Ruby
                           8.Saphire
                           9.Emerald
                           10.Fire red
                           11.Leaf Green
                           12.Diamond
                           13.Pearl
                           14.Platinum
                           15.HeartGold
                           16.SoulSilver
                           17.Black
                           18.White
                           19.Black 2
                           20.White 2
                           21.X
                           22.Y
                           23.Omega Ruby
                           24.Alpha Saphire
                           25.Sun
                           26.Moon
                           27.Ultra Sun
                           28.Ultra Moon
                           29.Sword
                           30.Shield
                           31.Brilliant Diamond
                           32.Shining Pearl
                           33.Legends Arceus
                           34.Scarlet
                           35.Violet""")
        #list of games, will take a while to add all of them becuase of all the quirks per game

        if gameChoice == "1" or gameChoice == "yellow" or gameChoice == "Yellow":

            gameSelection = 1
            #loop for game selecting is ended
            print("Yellow version selected")

            listSelect = Ymons
            #base list is selected
            preEvosGenSelect = preEvosGen1
            #selecting pre evoloution list
            legendSelectOperation(legendSelection)
            #operation for choosing whether to allow legendaries
            evoAllowSelect(evosAllowed, preEvosGenSelect, evoChoice)
            #operation to choose between per evoloutions or not
            tradeEvoOperation(tradeEvosSelection, evoChoice)
            #operation to choose to allow trade evoloutions, and add back mid stage evos if they wer removed as pre evos but cannot use trade evos
            gen1PostGameSelect(postGameAllowed, gameChoice, postGameList=None)
            # removal of post game pokemon if chosen
            gen1PorygonSelect(poryCheck)
            #choose to remove porygon because requirements to get pokemon are absurd
            teamSelectionAction(teamNoSelect, monSelect, selectCount=None)
            #final action to select the team members

        elif gameChoice == "Red" or gameChoice == "red" or gameChoice == "2":

            gameSelection = 1

            print("Red version Selected")

            listSelect = Rmons

            preEvosGenSelect = preEvosGen1

            legendSelectOperation(legendSelection)

            evoAllowSelect(evosAllowed, preEvosGenSelect, evoChoice)

            tradeEvoOperation(tradeEvosSelection, evoChoice)

            gen1PostGameSelect(postGameAllowed, gameChoice, postGameList = None)

            gen1PorygonSelect(poryCheck)

            teamSelectionAction(teamNoSelect, monSelect, selectCount=None)

        elif gameChoice == "3" or gameChoice == "Blue" or gameChoice == "blue":

            gameSelection = 1

            print("Blue version selected")

            listSelect = Bmons

            preEvosGenSelect = preEvosGen1

            legendSelectOperation(legendSelection)

            evoAllowSelect(evosAllowed, preEvosGenSelect, evoChoice)

            tradeEvoOperation(tradeEvosSelection, evoChoice)

            gen1PostGameSelect(postGameAllowed, gameChoice, postGameList = None)

            gen1PorygonSelect(poryCheck)

            teamSelectionAction(teamNoSelect, monSelect, selectCount=None)

        elif gameChoice == "gold" or gameChoice == "Gold" or gameChoice == "4":

            print("Gold version selected")

            listSelect = goldMons

            legendSelectOperation(legendSelection)

            evoAllowSelect(evosAllowed, preEvosGenSelect, evoChoice)

            tradeEvoOperation(tradeEvosSelection, evoChoice)





        else:

            print("Invalid option, please enter a game from the list")




print("Welcome to the pokemon team randomiser")

gameSelect(legends, preEvosGen1, evoChoice=None, monSelect=None)
