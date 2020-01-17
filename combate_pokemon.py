pokemon_elegido = input("Contra que pokemon vas a luchar (Squirtle/Charmander/Bulbasur) : ")

vida_pikachu = 100
nombre_pokemon = ""

vida_enemigo = 0
ataque_enemigo = 0

if pokemon_elegido == "Squirtle":
    nombre_pokemon = "Squirtle"
    vida_enemigo = 90
    ataque_enemigo = 8

elif pokemon_elegido == "Charmander":
    nombre_pokemon = "Charmander"
    vida_enemigo = 80
    ataque_enemigo = 7

elif pokemon_elegido == "Bulbasur":
    nombre_pokemon = "Bulbasur"
    vida_enemigo = 100
    ataque_enemigo = 10

while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("Que ataque vamos a usar (Chispazo/Bola Voltio)")
    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola Voltio":
        vida_enemigo -= 12
    print("Ahora {} tiene {}".format(nombre_pokemon,vida_enemigo))
    vida_pikachu -= ataque_enemigo
    print("{} ha realizado un ataque de {} dano ahora pikachu tiene {} de vida".format(nombre_pokemon,ataque_enemigo,vida_pikachu))

if vida_enemigo<=0 :
    print("Has ganadoo")
elif vida_pikachu<=0 :
    print("Has perdidp")

print("El combate a terminado")