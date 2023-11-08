import sympy as sp

def is_valid_function(func):
    try:
        x = sp.symbols('x')
        f = sp.sympify(func)
        df = sp.diff(f, x)
        return True
    except (sp.SympifyError, sp.SympifyError):
        return False

def validate_function_input():
    while True:
        func = input('Ingrese la función (por ejemplo, x**2 - 4): ')
        if is_valid_function(func):
            return func
        else:
            print('Error: Función no válida. Por favor, ingrese una función matemática válida.')

def validate_numeric_input(prompt, data_type, min_value=None, max_value=None):
    while True:
        try:
            value = data_type(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError
            return value
        except ValueError:
            print('Error: Ingrese un valor numérico válido dentro del rango permitido.')

def newton_method(func, x0, tolerance, max_iterations):
    for i in range(max_iterations):
        x = sp.symbols('x')
        try:
            f = sp.sympify(func)
            f_value = f.subs(x, x0).evalf()
        except sp.SympifyError:
            print('Error: La función no se pudo procesar correctamente.')
            return None

        if abs(f_value) < tolerance:
            print(f'Solución encontrada en la iteración {i}: x = {x0}')
            return x0

        df = sp.diff(f, x)
        try:
            df_value = df.subs(x, x0).evalf()
        except sp.SympifyError:
            print('Error: La derivada no se pudo calcular correctamente.')
            return None

        if df_value == 0:
            print('Error: La derivada se hizo cero. No se puede continuar.')
            return None

        x1 = x0 - f_value / df_value
        print(f'\nIteración {i}:')
        print('==================')
        print(f'x{i} = {x0}')
        print(f'f(x{i}) = {f_value}')
        print(f'f\'(x{i}) = {df_value}')
        print(f'x{i+1} = {x1}')
        print(f'Error absoluto: {abs(x1 - x0)}')

        if abs(x1 - x0) < tolerance:
            print(f'Solución convergente en la iteración {i}: x = {x1}')
            return x1

        x0 = x1

    print(f'El método de Newton no convergió después de {max_iterations} iteraciones.')
    return None

def main():
    func = validate_function_input()
    x0 = validate_numeric_input('Ingrese el valor inicial x0: ', float)
    tolerance = validate_numeric_input('Ingrese la tolerancia deseada: ', float, min_value=0.0)
    max_iterations = validate_numeric_input('Ingrese el número máximo de iteraciones: ', int, min_value=1)

    result = newton_method(func, x0, tolerance, max_iterations)

    if result is not None:
        print(f'La solución aproximada es x = {result}')

if __name__ == '__main__':
    main()
