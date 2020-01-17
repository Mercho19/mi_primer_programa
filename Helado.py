apetecer_helado = input("Se te antoja un helado ? ")

if apetecer_helado == "si":
    dinero_suficiente = int(input("Cuanto dinero tienes ?"))
    if dinero_suficiente >= 5:
        input("Entonces vamos a comprar el helado")
    else:
        input("Lastimosamente no tienes el dinero suficiente te faltan {} dolares D:".format(5 - dinero_suficiente))



if apetecer_helado == "no":
    input("Ok sera para la proxima")