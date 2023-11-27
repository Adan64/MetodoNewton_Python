from sympy import symbols, Eq, solve, lambdify
import numpy as np
import matplotlib.pyplot as plt

def interpolacion_por_sistema_de_ecuaciones(puntos, grado):
    # puntos es una lista de tuplas (x, y)
    x, y = zip(*puntos)

    # Definir las variables del polinomio
    a = symbols('a0:%d' % (grado + 2))

    # Construir el sistema de ecuaciones
    sistema_ecuaciones = [sum(a[i] * x_j**i for i in range(grado + 1)) - y_j for x_j, y_j in zip(x, y)]

    # Resolver el sistema
    solucion = solve(sistema_ecuaciones, a)

    # Extraer valores numéricos de las soluciones
    solucion_numericas = {k: v.evalf() for k, v in solucion.items()}

    # Construir el polinomio interpolante
    polinomio_interpolante = sum(solucion_numericas[a_i] * x**i for i, a_i in enumerate(a))

    return polinomio_interpolante

def main():
    # Obtener puntos del usuario
    puntos = []
    while True:
        entrada = input("Ingrese un punto como 'x,y' (o escriba 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        punto = tuple(map(float, entrada.split(',')))
        puntos.append(punto)

    # Obtener el grado del polinomio del usuario
    grado = int(input("Ingrese el grado del polinomio de interpolación: "))

    # Realizar interpolación
    polinomio = interpolacion_por_sistema_de_ecuaciones(puntos, grado)

    # Mostrar el polinomio interpolante
    print(f"El polinomio interpolante es: {polinomio}")

    # Graficar resultados
    x_vals = np.linspace(min(x for x, _ in puntos), max(x for x, _ in puntos), 100)
    y_vals = [polinomio.evalf(subs={symbols('x'): val}) for val in x_vals]

    plt.scatter(*zip(*puntos), label='Datos')
    plt.plot(x_vals, y_vals, label='Interpolación')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
