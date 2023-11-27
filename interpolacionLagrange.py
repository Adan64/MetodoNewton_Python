import sympy as sp

def lagrange_interpolation(points, x_value):
    x = sp.symbols('x')
    n = len(points)

    # Construir el polinomio interpolante de Lagrange
    lagrange_polynomials = []
    for i in range(n):
        numerator = sp.prod([(x - points[j][0]) for j in range(n) if j != i])
        denominator = sp.prod([(points[i][0] - points[j][0]) for j in range(n) if j != i])
        lagrange_polynomial_i = points[i][1] * numerator / denominator
        lagrange_polynomials.append(lagrange_polynomial_i)

    lagrange_polynomial = sp.simplify(sp.Add(*lagrange_polynomials))

    # Mostrar los polinomios de Lagrange intermedios
    for i, lag_poly in enumerate(lagrange_polynomials):
        print(f"L_{i}(x) = {lag_poly}")

    print("\nPolinomio interpolante de Lagrange:")
    print(f"P(x) = {lagrange_polynomial}")

    # Evaluar el polinomio interpolante en el valor de x dado
    result = lagrange_polynomial.subs(x, x_value)

    return result

def get_user_points():
    points = []
    while True:
        x_input = input("Ingrese el valor de x (deje en blanco para finalizar): ")
        if not x_input:
            break

        y_input = input(f"Ingrese el valor de y para x={x_input}: ")
        try:
            x_value = float(x_input)
            y_value = float(y_input)
            points.append((x_value, y_value))
        except ValueError:
            print("Error: Ingrese números válidos.")

    return points

def main():
    # Obtener los puntos de interpolación del usuario
    interpolation_points = get_user_points()

    # Valor de x para evaluar el polinomio interpolante
    x_value = float(input("Ingrese el valor de x para la evaluación del polinomio interpolante: "))

    # Realizar interpolación de Lagrange
    result = lagrange_interpolation(interpolation_points, x_value)

    print(f"\nEl resultado de la interpolación en x={x_value} es: {result}")

if __name__ == "__main__":
    main()
