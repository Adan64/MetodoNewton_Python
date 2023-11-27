import sympy as sp

def falsa_posicion(func, a, b, tol=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función 'func' en el intervalo [a, b] utilizando el método de la falsa posición.

    :param func: La función para la cual se busca la raíz.
    :param a: Extremo izquierdo del intervalo.
    :param b: Extremo derecho del intervalo.
    :param tol: Tolerancia para la convergencia (por defecto, 1e-6).
    :param max_iter: Número máximo de iteraciones (por defecto, 100).
    :return: Aproximación de la raíz, o None si no se cumple la tolerancia en el número máximo de iteraciones.
    """
    x = sp.symbols('x')
    func_expr = sp.sympify(func)

    # Definir el ancho de cada columna
    col_width = 14

    print(f"Iteration    |   a         |   b        |   f(a)       |   f(b)      |   x2       |  f(x2)    |")
    print("-" * (6 * col_width + 15))

    for i in range(max_iter):
        fa = func_expr.subs(x, a)
        fb = func_expr.subs(x, b)

        # Calcula el siguiente punto x2 usando la fórmula de la falsa posición.
        x2 = b - (fb * (b - a)) / (fb - fa)

        # Evalúa la función en x2.
        fx2 = func_expr.subs(x, x2)

        # Muestra los resultados de la iteración actual con formato alineado.
        print(f"{i+1:2}           | {a:.6f}".rjust(col_width + 2) + f" | {b:.6f}".rjust(col_width) + f" | {fa:.6f}".rjust(col_width) + f" | {fb:.6f}".rjust(col_width) + f" | {x2:.6f}".rjust(col_width) + f" | {fx2:.6f}".rjust(col_width) + " |")

        # Determina el nuevo intervalo.
        if abs(fx2) < tol:
            return x2  # Se encontró una raíz suficientemente cercana a cero.

        if fa * fx2 < 0:
            b = x2
        else:
            a = x2

    # Si no se alcanza la tolerancia en el número máximo de iteraciones, retorna None.
    return None

def main():
    try:
        # Solicita la función al usuario
        func_str = input("Ingrese la función (usando 'x' como variable): ")
        
        # Solicita el intervalo
        a = float(input("Ingrese el extremo izquierdo del intervalo: "))
        b = float(input("Ingrese el extremo derecho del intervalo: "))
        
        # Solicita la tolerancia
        tol = float(input("Ingrese la tolerancia: "))

        # Aplica el método de la falsa posición
        raiz_aproximada = falsa_posicion(func_str, a, b, tol)

        if raiz_aproximada is not None:
            print(f"\nAproximación de la raíz: {raiz_aproximada:.6f}")
        else:
            print("\nNo se pudo encontrar la raíz en el número máximo de iteraciones.")

    except (ValueError, sp.SympifyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
