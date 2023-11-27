import sympy as sp

def secante_solver():
    # Solicitar al usuario ingresar la función
    expresion = input("Ingrese la función f(x): ")

    # Convertir la expresión a una función simbólica
    try:
        x = sp.symbols('x')
        funcion = sp.sympify(expresion)
    except (sp.SympifyError, TypeError):
        print("Error al analizar la expresión. Asegúrate de ingresar una función válida.")
        return

    # Solicitar valores iniciales
    try:
        x0 = float(input("Ingrese el valor inicial x0: "))
        x1 = float(input("Ingrese el valor inicial x1: "))
    except ValueError:
        print("Error al ingresar valores iniciales. Asegúrate de ingresar números válidos.")
        return

    # Solicitar la tolerancia
    try:
        tol = float(input("Ingrese la tolerancia: "))
    except ValueError:
        print("Error al ingresar la tolerancia. Asegúrate de ingresar un número válido.")
        return

    # Definir la función evaluada
    f = sp.lambdify(x, funcion)

    # Inicializar variables
    iteraciones = 0

    # Imprimir encabezado
    print("\nIteración |   xk-1    |  f(xk-1)  |   xk     |   f(xk)  |    xk+1    |   f(xk+1)  |")

    while True:  # Continuar hasta que f(xk) sea menor a la tolerancia
        # Calcular el resultado de la función en x0
        f_x0 = f(x0)

        # Calcular el resultado de la función en x1
        f_x1 = f(x1)

        # Calcular el siguiente punto usando la fórmula de la secante
        x_next = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        # Calcular el resultado de la función en x_next
        f_x_next = f(x_next)

        # Imprimir valores calculados en esta iteración con 9 decimales y columnas intercambiadas
        print(f"{iteraciones : ^9} | {x0:.6f} | {f_x0:.6f} | {x1:.6f} | {f_x1:.6f} | {f_x_next:.6f} | {x_next:.6f} |")

        # Verificar convergencia
        if abs(f_x1) < tol:
            print("\nConvergencia alcanzada.")
            print(f"Aproximación de la raíz: {x1}")
            return

        # Actualizar valores para la siguiente iteración
        x0, x1 = x1, x_next
        iteraciones += 1

    # Este código nunca se alcanzará, pero lo incluyo por claridad
    print("\nEl método de la secante no convergió después de 100 iteraciones.")
    return

# Ejecutar el programa
secante_solver()
