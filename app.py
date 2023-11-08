import sympy as sp

def validate_input(func):
    try:
        sp.sympify(func)  # Intenta analizar la función
    except (sp.SympifyError, sp.DerivativeError) as e:
        print(f'Error al procesar la función: {e}')
        return None
    return func

def newton_method(func, x0, tolerance, max_iterations):
    x = sp.symbols('x')
    f = sp.sympify(func)
    df = sp.diff(f, x)

    for i in range(max_iterations):
        f_value = f.subs(x, x0).evalf()
        df_value = df.subs(x, x0).evalf()

        print(f'\nIteración {i}:')
        print('==================')
        print(f'x{i} = {x0}')
        print(f'f(x{i}) = {f_value}')
        print(f'f\'(x{i}) = {df_value}')

        if abs(f_value) < tolerance:
            print(f'Solución encontrada en la iteración {i}: x = {x0}')
            return x0

        if df_value == 0:
            print('La derivada se hizo cero. No se puede continuar.')
            return None

        x1 = x0 - f_value / df_value

        print(f'x{i+1} = {x1}')
        print(f'Error absoluto: {abs(x1 - x0)}')

        if abs(x1 - x0) < tolerance:
            print(f'Solución convergente en la iteración {i}: x = {x1}')
            return x1

        x0 = x1

    print(f'El método de Newton no convergió después de {max_iterations} iteraciones.')
    return None

def main():
    func = input('Ingrese la función (por ejemplo, x**2 - 4): ')
    x0 = float(input('Ingrese el valor inicial x0: '))
    tolerance = float(input('Ingrese la tolerancia deseada: '))
    max_iterations = int(input('Ingrese el número máximo de iteraciones: '))

    validated_func = validate_input(func)
    if validated_func is not None:
        result = newton_method(validated_func, x0, tolerance, max_iterations)

        if result is not None:
            print(f'La solución aproximada es x = {result}')

if __name__ == '__main__':
    main()
