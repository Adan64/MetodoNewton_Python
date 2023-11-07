import sympy as sp

def newton_method(func, x0, tolerance, max_iterations):
    x = sp.symbols('x')

    try:
        f = sp.sympify(func)
        df = sp.diff(f, x)
    except (sp.SympifyError, sp.DerivativeError):
        print('La función o su derivada no se pueden procesar.')
        return None

    for i in range(max_iterations):
        try:
            f_value = f.subs(x, x0).evalf()
            df_value = df.subs(x, x0).evalf()
        except (sp.SympifyError, sp.DerivativeError):
            print('La función o su derivada no se pueden evaluar en x0.')
            return None

        print(f'\nIteración {i}:')
        print(f'==================')
        print(f'x{i} = {x0}')
        print(f'f(x{i}) = {f_value}')
        print(f'f\'(x{i}) = {df_value}')

        if abs(f_value) < tolerance:
            print(f'Solución encontrada en la iteración {i}: x = {x0}')
            return x0

        if df_value == 0:
            print('La derivada se hizo cero. No se puede continuar.')
            return None

        try:
            x1 = x0 - f_value / df_value
        except (sp.SympifyError, sp.DerivativeError):
            print('Error al calcular la siguiente iteración.')
            return None

        print(f'x{i+1} = {x1}')
        print(f'Error absoluto: {abs(x1 - x0)}')

        if abs(x1 - x0) < tolerance:
            print(f'Solución convergente en la iteración {i}: x = {x1}')
            return x1

        x0 = x1

    print('El método de Newton no convergió después de', max_iterations, 'iteraciones.')
    return None

def main():
    func = input('Ingrese la función (por ejemplo, x**2 - 4): ')
    x0 = float(input('Ingrese el valor inicial x0: '))
    tolerance = float(input('Ingrese la tolerancia deseada: '))
    max_iterations = int(input('Ingrese el número máximo de iteraciones: '))

    result = newton_method(func, x0, tolerance, max_iterations)

    if result is not None:
        print(f'La solución aproximada es x = {result}')

main()