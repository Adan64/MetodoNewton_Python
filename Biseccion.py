import sympy as sp

def bisection_method(func, a, b, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, func)

    print("\nIteración\t   a\t\t   b\t\t   x\t\t  f(x)\t\t  b - a")
    print("="*80)

    iter_count = 0

    while iter_count < max_iter:
        x_val = (a + b) / 2
        fx = f(x_val)

        print(f"{iter_count}\t\t {a:.6f}\t {b:.6f}\t {x_val:.6f}\t {fx:.6f}\t {b - a:.6f}")

        if fx == 0 or abs(b - a) < tol:
            break
        elif f(a) * fx < 0:
            b = x_val
        else:
            a = x_val
        iter_count += 1

    root_approximation = (a + b) / 2
    return root_approximation, iter_count

def get_user_input():
    try:
        expression = input("Ingrese la función en términos de x: ")
        func = sp.sympify(expression)
        a = float(input("Ingrese el extremo izquierdo del intervalo (a): "))
        b = float(input("Ingrese el extremo derecho del intervalo (b): "))
        tolerance = float(input("Ingrese la tolerancia deseada: "))
        max_iterations = int(input("Ingrese el número máximo de iteraciones: "))
        return func, a, b, tolerance, max_iterations
    except (ValueError, sp.SympifyError) as e:
        print(f"Error: {e}")
        return None

def main():
    user_input = get_user_input()

    if user_input:
        func, a, b, tolerance, max_iterations = user_input
        print("\nResolviendo usando el método de la bisección:")
        print("=====================================================")
        print("Iteración\t   a\t\t   b\t\t   x\t\t  f(x)\t\t  b - a")
        print("="*80)
        root, iterations = bisection_method(func, a, b, tolerance, max_iterations)
        print("="*80)
        print(f"\nAproximación de la raíz: {root}")
        print(f"Número de iteraciones: {iterations}")

if __name__ == "__main__":
    main()
