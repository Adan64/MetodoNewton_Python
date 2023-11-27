import sympy as sp
import numpy as np

def find_iterative_function(f, x):
    f_prime = sp.diff(f, x)
    g = x - f / f_prime
    return g

def mil_solver(f, initial_guess, tolerance=1e-10, max_iterations=100):
    x = sp.symbols('x')

    # Convertir la función a sympy
    f = sp.sympify(f)

    # Encontrar la función iterativa
    g = find_iterative_function(f, x)

    # Convertir funciones a funciones numéricas
    f_func = sp.lambdify(x, f, 'numpy')
    g_func = sp.lambdify(x, g, 'numpy')

    # Inicializar variables
    x_old = initial_guess
    iterations = 0

    print(f"Iteration 0: x = {x_old}")

    # Iteraciones del método iterativo lineal
    while iterations < max_iterations:
        x_new = g_func(x_old)

        print(f"Iteration {iterations + 1}: x_new = {x_new}, f(x_new) = {f_func(x_new)}")

        # Criterio de convergencia
        if np.abs(x_new - x_old) < tolerance:
            print(f"Convergencia alcanzada en {iterations + 1} iteraciones.")
            return x_new, iterations

        x_old = x_new
        iterations += 1

    raise RuntimeError("El método iterativo no convergió en el número máximo de iteraciones.")

def main():
    try:
        # Solicitar la entrada del usuario
        equation_str = input("Ingrese la ecuación en términos de 'x': ")
        initial_guess = float(input("Ingrese el valor inicial de x: "))
        tolerance = float(input("Ingrese la tolerancia: "))

        # Resolver la ecuación
        solution, iterations = mil_solver(equation_str, initial_guess, tolerance)

        # Imprimir resultados
        print(f"Raíz aproximada encontrada: x = {solution}")
        print(f"Iteraciones realizadas: {iterations}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
