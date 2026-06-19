def devuelve_ciudades(*ciudades): # En python cuando colocamos un * delante del argument ode una funcion estamos indicando que va a rcibir un numero indeterminado
                                  # de elementos y ademas le estamos diciendo que se va a recibir en forma de tuple

    for elemento in ciudades:
        # for subElemento in elemento: # Esto vendria siendo un bucle for anidado osea un bucle for dentro de un bucle for
            yield from elemento # Pero aqui en este ejemplo con el Yield from vendria haciendo lo mismo que hace el for subElemento in elemento seria mas simplificado


ciudades_devueltas=devuelve_ciudades("Santo Domingo", "Madrid", "Bogota", " Miami")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))